from fastapi import FastAPI
from auth_routes import router as auth_router

from orm_routes import router


app = FastAPI()
app.include_router(router)
app.include_router(auth_router)
