import aiohttp
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from os import environ


load_dotenv()
app = FastAPI()
API_KEY = environ.get("API_KEY")


origins = [
    "http://localhost:8081",
]

# https://fastapi.tiangolo.com/tutorial/cors/
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
        "Authorization": f"Token {API_KEY}"
    }
    params = {
        "q": passage,
        "include-passage-references": "false",
        "include-footnotes": "false",
        "include-headings": "false",
        "include-short-copyright": "false"
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, params=params) as resp:
            response = await resp.json()
            return response["passages"][0]
