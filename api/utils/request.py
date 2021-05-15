import aiohttp
from dotenv import load_dotenv

from os import environ


__all__ = ["request"]


load_dotenv()
API_KEY = environ.get("API_KEY")


async def request(passage: str):
    url = "https://api.esv.org/v3/passage/text/"

    # TODO: move authorization to dependencies?
    headers = {
        "accept": "application/json",
        "Authorization": f"Token {API_KEY}",
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
