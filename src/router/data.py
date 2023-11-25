from fastapi import APIRouter

import impl.views as views


data_router = APIRouter(
    prefix='/data',
    tags=['Data'],
    responses={404: {'detail': 'Not found'}},
)


@data_router.get('/')
async def handler_data_get():
    """Ручка получения информации о данных"""
    response = await views.data.handler_get.data_get_impl()
    return response


@data_router.post('/')
async def handler_data_post():
    """Ручка добавления данных"""
    response = await views.data.handler_post.data_post_impl()
    return response
