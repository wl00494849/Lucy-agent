from string import Template
from pathlib import Path

def markdownTemplateReader(path:str)->Template:
    with open(path,"r",encoding="utf-8") as f:
        t = Template(f.read())
    return t

def markdownReader(path:str)->str:
    print(Path(path).suffix)
    if Path(path).suffix == ".md":
        with open(path,"r",encoding="utf-8") as f:
            return f.read()
    else:
        return "Not markdown file"
