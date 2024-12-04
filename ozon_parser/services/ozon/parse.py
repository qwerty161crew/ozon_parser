from uuid import uuid4

from ozon_parser.db import TaskRepository, get_repository
from ozon_parser.schema import (
    CheckTaskStatus,
    CreateTaskParser,
    ResponeCheckTask,
    ResponseIdTask,
)
from ozon_parser.schema.ozon import OzonProduct
from ozon_parser.worker import Publisher, get_publisher


class ParserService:
    def __init__(self, publisher: Publisher, task_repository: TaskRepository):
        self.publisher = publisher
        self.task_repository = task_repository

    async def create_task(self, parse_condition: CreateTaskParser) -> ResponseIdTask:
        task_id = uuid4()
        await self.task_repository.create_task(task_id=task_id)
        publish_message = {
            "job_id": str(task_id),
            "start_url": parse_condition.start_url,
            "product_type": parse_condition.product_type,
        }
        # await self.publisher.publish_message(
        #     message=publish_message, routing_key="ozon_api"
        # )

        async with self.publisher as producer:
            await producer.publish_message(
                message=publish_message, routing_key="ozon_api"
            )
        return ResponseIdTask(task_id=task_id)

    async def check_task(self, check_status: CheckTaskStatus) -> ResponeCheckTask:
        task = await self.task_repository.get(task_id=check_status.task_id)
        if task:
            return ResponeCheckTask(
                task_id=task.task_id, message=task.message, state=task.state
            )

    async def get_the_parsing_result(self, task_id: str) -> list[OzonProduct]:
        pass


async def get_parser_service() -> ParserService:
    publisher = await get_publisher()
    task_repository = await get_repository()
    return ParserService(publisher=publisher, task_repository=task_repository)


async def get_parser_service() -> ParserService:
    publisher = await get_publisher()
    task_repository = await get_repository()
    return ParserService(publisher=publisher, task_repository=task_repository)
