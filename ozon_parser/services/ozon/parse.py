from ozon_parser.schema import CheckTaskStatus, CreateTaskParser, ReposneIdTask
from ozon_parser.schema.ozon import OzonProduct


class ParserService:
    def __init__(self):
        pass

    async def create_task(self, parse_condition: CreateTaskParser) -> ReposneIdTask:
        pass

    async def check_task(self, check_status: CheckTaskStatus) -> CheckTaskStatus:
        pass

    async def get_the_parsing_result(self, task_id: str) -> list[OzonProduct]:
        pass


async def get_parser_service() -> ParserService:
    return ParserService()
