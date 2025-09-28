from fastapi import APIRouter,Response
from src.LLMs import LLMs

gpt_router = APIRouter(prefix="/gpt",tags=["LLMs"])
health_router = APIRouter(prefix="/health",tags=["HEALTH"])

@gpt_router.post("/")
async def gpt(item:LLMs.LineBot_Requset):
    try:
        gpt = LLMs()
        resp = gpt.request(item=item)
        return {"response":resp}
    except Exception as e:
        print(f"GPT Error:{e}")

@health_router.get("/live")
async def live():
    try:
        return Response(content="ok",status_code=200)
    except:
        print("program crush")
