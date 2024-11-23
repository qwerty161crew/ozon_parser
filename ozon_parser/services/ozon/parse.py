import asyncio

from httpx import AsyncClient
from playwright.async_api import async_playwright

from ozon_parser.adapter.ozon import OzonParser, get_ozon_parser
from ozon_parser.schema import GreatOfferParser


class ParserService:
    def __init__(self, parser: OzonParser, http_client: AsyncClient):
        self.parser = parser
        self.http_client = http_client

    async def get_great_offers_in_ozon(self, parse_condition: GreatOfferParser) -> None:
        async with async_playwright() as playwright:
            browser = await playwright.firefox.launch()
            print(browser)


async def get_parser_service() -> ParserService:
    # adapter = await get_httpx_adapter()
    ozon_parser = await get_ozon_parser()
    return ParserService(http_client=AsyncClient(), parser=ozon_parser)
