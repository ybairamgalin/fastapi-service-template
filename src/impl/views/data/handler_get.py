from fastapi import Response


async def data_get_impl():
    return Response(status_code=200)
