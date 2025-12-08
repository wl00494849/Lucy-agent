from langchain_text_splitters import MarkdownHeaderTextSplitter
from src.reader import markdownReader
from pathlib import Path

## markdown Hierarchical Routing
def markdownSplitter(path:str):

    headers_to_split_on = [
        ("#", "Header1"),
        ("##", "Header2"),
        ("###", "Header3"),
    ]

    content = markdownReader(path=path)
    markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on)
    splitter_text = markdown_splitter.split_text(text=content)

    return splitter_text




