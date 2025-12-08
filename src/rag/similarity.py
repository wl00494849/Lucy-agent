import logging
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from src.LLMs import LLMs

## 取得餘弦相似度
def get_cosine_similarity(term1:str,term2:str,size:int=0)->float:
        gpt = LLMs()

        print(f"term1:{term1},term2:{term2}")
        
        response1 = gpt.vector(term1,size)[0].embedding
        response2 = gpt.vector(term2,size)[0].embedding

        cos = calcute_cos(response1,response2)

        print(f"cosine_similarity:{cos}")

        return cos

## 計算餘弦相似度
def calcute_cos(vector1,vector2)->float:
        di1 = np.array([vector1]).reshape(1, -1)
        di2 = np.array([vector2]).reshape(1, -1)
        cos = cosine_similarity(di1,di2)
        return cos
