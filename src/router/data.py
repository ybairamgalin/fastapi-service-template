from fastapi import APIRouter

import impl.views as views
from router.models import data_models


data_router = APIRouter(
    prefix='/data',
    tags=['Data'],
    responses={404: {'detail': 'Not found'}},
)


@data_router.get('/')
async def handler_data_get() -> list[data_models.Item]:
    """Ручка получения информации о данных"""
    response = await views.data.handler_get.data_get_impl()
    return response


@data_router.post('/')
async def handler_data_post(name: str):
    """Ручка добавления данных"""
    response = await views.data.handler_post.data_post_impl(name)
    return response
