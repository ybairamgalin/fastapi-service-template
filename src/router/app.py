from fastapi import APIRouter

from router.data import data_router

app_router = APIRouter()

app_router.include_router(data_router)
