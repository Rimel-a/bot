from urllib.parse import quote as quote_url

import aiohttp

from .constants import Keys, URLs


class APIClient:
    def __init__(self, **kwargs):
        auth_headers = {
            'Authorization': f"Token {Keys.site_api}"
        }

        if 'headers' in kwargs:
            kwargs['headers'].update(auth_headers)
        else:
            kwargs['headers'] = auth_headers

        self.session = aiohttp.ClientSession(
            **kwargs,
            raise_for_status=True
        )

    @staticmethod
    def _url_for(endpoint: str):
        return f"{URLs.site_schema}{URLs.site_api}/{quote_url(endpoint)}"

    async def get(self, endpoint: str, *args, **kwargs):
        async with self.session.get(self._url_for(endpoint), *args, **kwargs) as resp:
            return await resp.json()
