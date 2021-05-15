from api.config import cfg

import aiohttp


__all__ = ["request"]


url = "https://api.esv.org/v3/passage/text/"
api_key = cfg.esv_api.api_key.get_secret_value()


async def request(passage: str):
    # TODO: move authorization to dependencies?
    headers = {
        "accept": "application/json",
        "Authorization": f"Token {api_key}",
    }

    params = {
        "q": passage,
        "include-passage-references": "false",
        "include-footnotes": "false",
        "include-headings": "false",
        "include-short-copyright": "false",
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(
            url, headers=headers, params=params
        ) as resp:
            response = await resp.json()
            return response
