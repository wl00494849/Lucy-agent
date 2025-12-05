from string import Template

def markdownReader(path:str)->Template:
    with open(path,"r",encoding="utf-8") as f:
        t = Template(f.read())
    return t