from fastapi import FastAPI
from database import engine, Base

from routers.webhook import router as webhook_router
from routers.auth import router as auth_router

app = FastAPI()

app.include_router(webhook_router)
app.include_router(auth_router)

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

@app.get("/")
def health():
    return {"status": "ok"}
