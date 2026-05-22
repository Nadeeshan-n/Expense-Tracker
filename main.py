from fastapi import FastAPI

from orm_routes import router


app = FastAPI()
app.include_router(router)
