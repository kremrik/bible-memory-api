from api.middleware.cors import CORS

import aiohttp
from dotenv import load_dotenv
from fastapi import FastAPI

from os import environ


load_dotenv()
API_KEY = environ.get("API_KEY")


app = FastAPI()
app.add_middleware(**CORS)


@app.get("/passage/{passage}")
async def passage(passage: str):
    response = await request(passage)
    return {"data": response}


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
            return response["passages"][0]
