from src.reader import markdownTemplateReader
from src.rag.chunker import markdownSplitter
from src.rag.similarity import get_cosine_similarity
from src.rag.heap import max_heap,kv
import os

def rag(question:str)->str:

    print(f"問題：{question}")
    print("=========================================")

    heap = max_heap()
    filepath = select_relation_file(question=question)
    chunks = markdownSplitter(filepath)

    print("=========================================")
    print("HyDE")
    hyDE = generate_hyde_document(question)
    print("=========================================")

    for c in chunks:
        if c.page_content != "":
            cos = get_cosine_similarity(hyDE,c.page_content)
            val = kv(k=c.page_content,v=cos)
            heap.push(val)
        print("cosine_similarity")
        print(cos)
        print(c.page_content)
        print("=========================================")

    ## top 1
    information = heap.pop().k

    t = markdownTemplateReader("prompts/rag/rag_prompt.md")
    prompt = t.substitute(
        question = question,
        information = information
    )

    return prompt

## 遍歷data資料夾
def data_traversal()->tuple[str,list]:
    root = "data"
    fileName_list = ""
    file_maps = {}

    for dirpath,dirnames,filenames in os.walk(root):
        print(dirpath)
        for dir in dirnames:
            print(f"-子目錄：{dir}")
        for f in filenames:
            print(f"--檔案名稱：{f}")
            fileName_list += f + "\n"
            file_maps[f] = dirpath + "/" + f
        print("=========================================")

    return fileName_list,file_maps

## HyDE
def generate_hyde_document(query:str)->str:
    from src.LLMs import LLMs
    gpt = LLMs()
    prompt = f"針對以下問題，生成一小段可能存在的文件內容：\n\n{query}\n"
    hyDE = gpt.request(prompt)
    print(hyDE)
    return hyDE

## 找出相關檔案
def select_relation_file(question:str)->str:
    from src.LLMs import LLMs

    fileName_list,file_maps = data_traversal()
    t = markdownTemplateReader("prompts/rag/rag_relation.md")
    prompt = t.substitute(
        fileName_list = fileName_list,
        question = question
    )

    gpt = LLMs()
    result = gpt.request(prompt)
    print(f"相關檔案：{result}")

    filepath = file_maps[result]

    return filepath


