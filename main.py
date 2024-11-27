import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI

from data.cotizaciones import fetch_data, refresh_data
from routers import dolar_service
from utils.cleanup import gc_collect


@asynccontextmanager
async def startup_and_shutdown(app: FastAPI):
    await fetch_data()
    loop = asyncio.get_event_loop()
    loop.create_task(refresh_data())
    loop.create_task(gc_collect())
    yield


app = FastAPI(lifespan=startup_and_shutdown)
app.include_router(dolar_service.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
