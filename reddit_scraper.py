from time import sleep
import requests
from fake_useragent import UserAgent
from sqlalchemy.exc import DBAPIError,PendingRollbackError
from table import session,posts as post_obj
import logging

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.WARNING)

ua = UserAgent()
user_agent = ua.chrome
secret = "THUoHkeIYjeJEwSiyNDVmmVhZj_K-Q"
client_id = "6zRu_vdjCXJpMB3vzKNJ0w"
user_name = "aammirzaei"
password = "@m1r@rsh1@"
auth = requests.auth.HTTPBasicAuth(client_id, secret)
data = {"grant_type":"password","username":user_name,"password":password}
res = requests.post("https://www.reddit.com/api/v1/access_token",auth=auth,data=data,headers={"User-Agent":user_agent})
tocken = res.json()
s = tocken['access_token']
header = {"Authorization": f"bearer {s}","User_Agent": user_agent}


while True:
    response = requests.get("https://oauth.reddit.com/r/nextfuckinglevel/hot",headers=header,params={"limit":"10"})
    if str(response) == "<Response [429]>":
        print(response)
        sleep(10)
        continue
    else:
        posts =response.json()['data']['children']
        for post in posts:
            if post["data"]["url"].startswith("https://i.redd.it/"):
                name =post["data"]["title"][:10]
                url = post["data"]["url"]
                sub_reddit =post["data"]["subreddit"]
                try:
                    session.add(post_obj(name=name,url=url,sub_reddit=sub_reddit))
                    session.commit()
                except (DBAPIError,PendingRollbackError):
                    print("duplicate")
                    pass
            else:
                print(post["data"]["url"])
    break