import requests
from os import chdir,mkdir
from table import P_name
from engine import session
from fake_useragent import UserAgent
from serpapi import GoogleSearch
ua = UserAgent()
chdir("images")

IN_list = session.query(P_name).all()

def get_url(name):
    params = {
        "api_key":"690f2872610f796863fc0466211d57fbe3e6952a405b79be91b0afb7626303ef",
        "q": name,
        "tbm": "isch",
        "ijn": "0",
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    images_results = results['images_results'][0]["original"]
    return images_results

def download(url,image_name):
    try:
        d = requests.get(url,stream=True,headers={"User-Agent":ua.chrome})
        mkdir(image_name)

        with open(f"{image_name}/{image_name}.jpg", 'wb')as f:
            for chunk in d.iter_content(4096):
                if not chunk:
                    print("breaked")
                    break
                f.write(chunk)
            print(image_name)   
    except:
        print("connection Error")
        pass
print(len(IN_list[253:]))
    

