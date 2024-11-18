class ParserService:
    def __init__(self, parser, repository):
        self.parser = parser
        self.repository = repository


async def get_parser_service() -> ParserService:
    return ParserService()
