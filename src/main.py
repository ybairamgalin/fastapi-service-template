from fastapi import FastAPI
from fastapi import Response

import router
import dependencies

app = FastAPI()
app.include_router(router.app_router)
dependencies.init_dependencies()


@app.get('/ping')
def handler_ping_get():
    """Ping handler needed for healthcheck"""
    return Response(status_code=200)
