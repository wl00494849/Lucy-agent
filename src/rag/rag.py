from src.reader import markdownReader
from src.LLMs import LLMs
from langchain_text_splitters import MarkdownHeaderTextSplitter
import os

def exec_rag(question:str):

    t = markdownReader("prompts/rag/rag_prompt.md")
    information = ""
    prompt = t.substitute(
        question=question,
        information=information
    )

## 遍歷data資料夾
def topN_search()->str:
    root = "data"
    prompt = ""
    files_map = []

    for dirpath,dirnames,filenames in os.walk(root):
        for f in filenames:
            prompt += dirpath + "/" + f + "\n"
            

    return prompt


