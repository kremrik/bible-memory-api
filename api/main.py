from api.auth import router
from api.middleware.cors import CORS
from app.parse_to_hints import chapter_to_hints, Chapter

import aiohttp
from dotenv import load_dotenv
from fastapi import FastAPI

from os import environ


load_dotenv()
API_KEY = environ.get("API_KEY")


app = FastAPI()
app.include_router(router)
app.add_middleware(**CORS)


@app.get("/passage/{passage}", response_model=Chapter)
async def passage(passage: str, hint_min: int = 3):
    response = await request(passage)
    chapter = 3
    data = chapter_to_hints(
        passage=response["passages"][0],
        chapter=chapter,
        hint_min=hint_min
    )
    return data


@app.get("/")
async def root():
    return {"message": __file__}


async def request(passage: str):
    url = "https://api.esv.org/v3/passage/text/"
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
