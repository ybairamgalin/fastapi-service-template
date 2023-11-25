from fastapi import Response


async def data_post_impl():
    return Response(status_code=201)
