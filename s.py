from time import sleep
import requests
from table import session,posts
from fake_useragent import FakeUserAgent

p = session.query(posts).all()
x =p[3]
ua = FakeUserAgent()

def down(url,name):
    res = requests.get(url)
    total = int(res.headers["Content-Length"])
    current = 0
    with open(name+"."+res.headers["Content-Type"][6:],"wb")as f:
        for chuncks in res.iter_content(chunk_size= 512):
            current +=len(chuncks)
            print(f"downloading {current} from {total} : {current*100/total}% ",end="\r")
            f.write(chuncks)

down(x.url,x.name)
