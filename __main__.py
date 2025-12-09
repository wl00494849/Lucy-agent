from fastapi import FastAPI
from src.router.api_v1 import gpt_router ,health_router

app = FastAPI()

app.include_router(gpt_router)
app.include_router(health_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,port=8000,host="0.0.0.0")