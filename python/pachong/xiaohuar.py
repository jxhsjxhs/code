import json,requests,os,lxml,time
from  bs4  import  BeautifulSoup

rul_list = []
img_list=[]

url = "http://www.xiaohuar.com/p-1-{}.html"
for i in range(2065):
    res = requests.get(url.format(i + 1))
    if res.status_code == 200:
        try:
            soup = BeautifulSoup(res.text, 'lxml')
            req = soup.img.get("src")
            img_url = "http://www.xiaohuar.com" + req
            print(img_url)
            img_list.append(img_url)
            pic = requests.get(img_url,timeout=5)
            fp = open("img/" + str(i) + ".jpg",'wb')
            fp.write(pic.content)
            fp.close()
        except :
            continue


