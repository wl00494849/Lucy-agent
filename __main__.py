from fastapi import FastAPI
from router.api_v1 import LLMs_router ,health_router
import logging

app = FastAPI()
app.include_router(LLMs_router)
app.include_router(health_router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,port=8000,host="0.0.0.0")