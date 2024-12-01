import asyncio

import aio_pika
import aio_pika.abc
from aio_pika import Message, connect_robust
from aio_pika.robust_connection import AbstractRobustConnection

from ozon_parser.config import config
from ozon_parser.db import TaskRepository, get_repository


class Consumer:
    def __init__(self, host, port, user, password, repository: TaskRepository):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.connect: AbstractRobustConnection | None = None
        self.repository = repository

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

    async def listen(self, loop):
        async with self.connect:
            queue_name = "parse_result"
            channel: aio_pika.abc.AbstractChannel = await self.connect.channel()
            queue: aio_pika.abc.AbstractQueue = await channel.declare_queue(
                queue_name, auto_delete=False
            )

            async with queue.iterator() as queue_iter:
                async for message in queue_iter:
                    async with message.process():
                        result = message.body.decode()
                        print(result)


async def main(loop):
    """
    RESPONSE Parser
    {
    "task_id": UUID,
    "state": "Complete",
    "Message": "Complete"
    }
    """
    repository = await get_repository()
    async with Consumer(
        user=config.rabbig_mq.user,
        host=config.rabbig_mq.host,
        port=config.rabbig_mq.port,
        password=config.rabbig_mq.password,
        repository=repository,
    ) as consumer:
        await consumer.listen(loop)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    loop.close()
