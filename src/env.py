import os

def load_env(path:str=".env"):
    if os.path.exists(path=path):
        with open(path,'r') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if "=" not in line:
                    continue
                key,val = line.split("=",1)
                key= key.strip()
                val= val.strip().strip('"').strip("'")
                os.environ[key]=val