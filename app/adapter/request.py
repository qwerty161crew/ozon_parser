from typing import Union

from httpx import AsyncClient


class HttpxAdapter:
    def __init__(self, session: AsyncClient):
        self.session = session

    async def fetch_page(self, url: str) -> Union[str, False]:
        async with self.session as client:
            try:
                response = await client.get(url)
                return response.text
            except Exception:
                return False


async def get_httpx_adapter():
    return HttpxAdapter(AsyncClient())
