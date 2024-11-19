from httpx import AsyncClient

from adapter.ozon import get_ozon_parser, OzonParser
from schema import GreatOfferParser


class ParserService:
    def __init__(self, parser: OzonParser, repository, http_client: AsyncClient):
        self.parser = parser
        self.repository = repository
        self.http_client = http_client

    async def get_great_offers_in_ozon(self, parse_condition: GreatOfferParser) -> None:
        response_text = await self.http_client.get(
            url="https://www.ozon.ru/highlight/globalpromo/"
        )
        if response_text:
            great_offers = self.parser.parse_great_offers(
                response_text, limit=parse_condition.limit
            )
            # await self.repository.save_great_offers(great_offers)


async def get_parser_service() -> ParserService:
    # adapter = await get_httpx_adapter()
    ozon_parser = await get_ozon_parser()
    return ParserService(http_adapter=AsyncClient(), parser=ozon_parser)
