from api.routes.auth import router as auth  # type: ignore
from api.routes.passages import router as passages  # type: ignore
from api.middleware.cors import CORS

from fastapi import FastAPI


app = FastAPI()

app.include_router(passages)
app.include_router(auth)

app.add_middleware(**CORS)  # type: ignore


@app.get("/")
async def root():
    return {"message": __file__}
