from langchain_text_splitters import MarkdownHeaderTextSplitter
from langchain_core.documents import Document
from src.reader import markdownReader

## markdown Hierarchical Routing
def markdownSplitter(path:str)->list[Document]:

    headers_to_split_on = [
        ("#", "Header1"),
        ("##", "Header2"),
        ("###", "Header3"),
    ]

    content = markdownReader(path=path)
    markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on)
    splitter_text = markdown_splitter.split_text(text=content)

    return splitter_text




