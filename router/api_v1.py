from fastapi import APIRouter
from src.LLMs import LLMs

router = APIRouter(prefix="/gpt",tags=["LLMs"])

@router.post("/")
async def gpt(item:LLMs.LineBot_Requset):
    gpt = LLMs()
    resp = gpt.request(item=item)
    return {"response":resp}
