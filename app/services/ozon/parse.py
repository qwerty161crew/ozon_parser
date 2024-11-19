from adapter import get_httpx_adapter, HttpxAdapter
from schema import GreatOfferParser

class ParserService:
    def __init__(self, parser, repository, http_adapter: HttpxAdapter):
        self.parser = parser
        self.repository = repository
        self.http_adapter = http_adapter

    async def get_great_offers_in_ozon(self, parse_condition: GreatOfferParser) -> None:
        response_text = await self.http_adapter.fetch_page(
            url="https://www.ozon.ru/highlight/globalpromo/"
        )
        if response_text:
            great_offers = self.parser.parse_great_offers(response_text, parse_condition)
            # await self.repository.save_great_offers(great_offers)


async def get_parser_service() -> ParserService:
    adapter = await get_httpx_adapter()
    return ParserService(http_adapter=adapter)
