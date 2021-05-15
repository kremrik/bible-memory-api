from api import __version__
from api.routes.auth import router as auth  # type: ignore
from api.routes.passages import router as passages  # type: ignore
from api.routes.users import router as users  # type: ignore
from api.middleware.cors import CORS

from fastapi import FastAPI


app = FastAPI()

app.include_router(passages)
app.include_router(auth)
app.include_router(users)

app.add_middleware(**CORS)  # type: ignore


@app.get("/")
async def root():
    return {"message": __file__, "version": __version__}


@app.get("/status")
async def status():
    return "ACTIVE"
