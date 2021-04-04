from api.auth import router as auth, validate_token
from api.middleware.cors import CORS
from app.passage import get_passage, BibleResponse

import aiohttp
from dotenv import load_dotenv
from fastapi import FastAPI, Depends

from os import environ


load_dotenv()
API_KEY = environ.get("API_KEY")


app = FastAPI()
app.include_router(auth)
app.add_middleware(**CORS)  # type: ignore


@app.get(
    "/passage/{passage}", response_model=BibleResponse
)
async def passage(
    passage: str,
    user: str = Depends(validate_token),
):
    response = await request(passage)
    data = get_passage(response)
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
