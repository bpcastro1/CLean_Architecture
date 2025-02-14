from fastapi import FastAPI
from app.interfaces.api.routes import router
from app.infrastructure.database.database import engine, Base

app = FastAPI(title="Bookstore API", version="1.0.0")

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(router, prefix="/api/v1") 