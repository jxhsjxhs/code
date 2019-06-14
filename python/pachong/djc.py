import json,requests,os,lxml,time
from  bs4  import  BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

URLS = []
img_list=[]

url = "http://www.xiaohuar.com/p-1-{}.html"
for i in range(2065):
    res = url.format(i + 1)
    URLS.append(res)


def load_url(url):
    for i in range(2065):
        res = requests.get(url.format(i + 1))
        if res.status_code == 200:
            try:
                soup = BeautifulSoup(res.text, 'lxml')
                req = soup.img.get("src")
                img_url = "http://www.xiaohuar.com" + req
                print(soup.title.string)
                print(img_url)
                img_list.append(img_url)
                pic = requests.get(img_url,timeout=5)
                fp = open("img/" + str(soup.title.string) + ".jpg",'wb')
                fp.write(pic.content)
                fp.close()
            except :
                pass
        URLS.remove(res)
try:
    executor = ThreadPoolExecutor(max_workers=64)
    executor.map(load_url,URLS)
    print('主线程结束')
except :
        pass
