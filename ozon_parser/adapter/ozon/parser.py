from bs4 import BeautifulSoup
from playwright.async_api import async_playwright


class OzonParser:
    def __init__(self, bs4: BeautifulSoup):
        self.bs4 = bs4

    def parse_great_offers(self, str_page: str, limit: int):
        pass

    def _fetch_product_url(self, rule: str):
        pass


async def get_ozon_parser():
    return OzonParser(bs4=BeautifulSoup())