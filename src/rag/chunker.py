import re
from typing import List

def markdown_chunker_byheading(text:str):
    ## split by head# 1~6
    parts = re.split(r'(?m)(^#{1,6} .*$)',text)
    chunks = []


