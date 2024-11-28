from ozon_parser.db import get_repository
from ozon_parser.schema import CheckTaskStatus, CreateTaskParser, ReposneIdTask
from ozon_parser.schema.ozon import OzonProduct
from ozon_parser.worker import Publisher, get_publisher


class ParserService:
    def __init__(self, publisher: Publisher):
        pass

    async def create_task(self, parse_condition: CreateTaskParser) -> ReposneIdTask:
        pass

    async def check_task(self, check_status: CheckTaskStatus) -> CheckTaskStatus:
        pass

    async def get_the_parsing_result(self, task_id: str) -> list[OzonProduct]:
        pass


async def get_parser_service() -> ParserService:
    publisher = await get_publisher()
    return ParserService(publisher=publisher)
