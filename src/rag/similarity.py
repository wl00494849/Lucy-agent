import numpy as np
from src.LLMs import LLMs

## 取得餘弦相似度
def get_cosine_similarity(term1:str,term2:str,size:int=0)->float:
        gpt = LLMs()
        
        response1 = gpt.vector(term1,size)[0].embedding
        response2 = gpt.vector(term2,size)[0].embedding

        cos = cosine_similarity(response1,response2)

        return cos

## 計算餘弦相似度
def cosine_similarity(vec1, vec2):
    dot = np.dot(vec1, vec2)
    return dot / (np.linalg.norm(vec1) * np.linalg.norm(vec2))