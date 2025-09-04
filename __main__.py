from fastapi import FastAPI
from router.api_v1 import router as LLMs
import logging

app = FastAPI()
app.include_router(LLMs)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,port=8000,host="0.0.0.0")