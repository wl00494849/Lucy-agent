from fastapi import FastAPI
from src.env import load_env
from src.LLMs import LLMs

app = FastAPI()
gpt = LLMs()
load_env()

@app.post("/gpt")
def gpt(item:LLMs.LineBot_Requset):
    resp = gpt.request(item=item)
    return {"response":resp}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,port=8000,host="0.0.0.0")