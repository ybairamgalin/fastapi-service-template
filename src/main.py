from fastapi import FastAPI
from fastapi import Response

import router

app = FastAPI()
app.include_router(router.app_router)
