import asyncio
import json
import uuid

import aio_pika.abc
from aio_pika import Message, connect_robust
from aio_pika.robust_connection import AbstractRobustConnection

from ozon_parser.config import config


class Publisher:
    def __init__(self, host, port, user, password):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.connect: AbstractRobustConnection | None = None

    async def create_connection(self):
        if self.connect is None:
            self.connect = await connect_robust(
                f"amqp://{self.user}:{self.password}@{self.host}:{self.port}/",
            )

    async def close_connection(self):

        if self.connect is not None:
            await self.connect.close()

    async def __aenter__(self):
        await self.create_connection()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close_connection()

    async def publish_message(
        self,
        routing_key: str,
        message: dict[str, list[dict] | str],
    ) -> None:
        """
        {
        'job_id': uuid.uuid4(),
        'start_url': "",
        'product_type': "",
        }
        """
        channel: aio_pika.abc.AbstractChannel = await self.connect.channel()

        async with self.connect:
            await channel.default_exchange.publish(
                Message(body=json.dumps(message).encode("utf-8")),
                routing_key=routing_key,
            )


async def get_publisher():
    print(config.rabbig_mq)
    return Publisher(
        user=config.rabbig_mq.user,
        host=config.rabbig_mq.host,
        port=config.rabbig_mq.port,
        password=config.rabbig_mq.password,
    )
