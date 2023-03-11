from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routes.routes import router


app = FastAPI()
app.include_router(router)
app.mount('/static', StaticFiles(directory='app/static'), name='static')
