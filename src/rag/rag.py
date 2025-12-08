from src.reader import markdownTemplateReader
from src.LLMs import LLMs
from src.rag.chunker import markdownSplitter
from src.rag.similarity import get_cosine_similarity
from src.rag.heap import max_heap,kv
import os


def exec_rag(question:str)->str:

    gpt = LLMs()
    heap = max_heap()

    filepath = select_relation_file(question=question)
    chunks = markdownSplitter(filepath)
    hyDE = generate_hyde_document(question)

    for c in chunks:
        cos = get_cosine_similarity(hyDE,c.page_content)
        val = kv(k=c.page_content,v=cos)
        heap.push(val)

        print(cos)

    information = heap.pop().k
    
    t = markdownTemplateReader("prompts/rag/rag_prompt.md")
    prompt = t.substitute(
        question = question,
        information = information
    )

    return gpt.request(prompt)

## 遍歷data資料夾
def data_traversal()->tuple[str,list]:

    root = "data"
    fileName_list = ""
    file_maps = {}

    for dirpath,dirnames,filenames in os.walk(root):
        for f in filenames:
            fileName_list += f + "\n"
            file_maps[f] = dirpath + "/" + f

    return fileName_list,file_maps

## HyDE
def generate_hyde_document(query:str)->str:
    gpt = LLMs()
    prompt = f"針對以下問題，生成一小段可能存在的文件內容：\n\n{query}\n"
    hyDE = gpt.request(prompt)
    print(hyDE)
    return hyDE

## 找出相關檔案
def select_relation_file(question:str)->str:

    fileName_list,file_maps = data_traversal()

    t = markdownTemplateReader("prompts/rag/rag_relation.md")
    prompt = t.substitute(
        fileName_list = fileName_list,
        question = question
    )

    gpt = LLMs()
    result = gpt.request(prompt)
    filepath = file_maps[result]

    return filepath


