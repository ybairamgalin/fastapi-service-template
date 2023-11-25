from fastapi import FastAPI
from fastapi import Response

import router

app = FastAPI()
app.include_router(router.app_router)


@app.get('/ping')
def handler_ping_get():
    return Response(status_code=200)
