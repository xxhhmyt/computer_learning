import requests
from  bs4 import BeautifulSoup  as bs

url = "http://www.netbian.com/weimei/"
res = requests.get(url)
res.encoding = "gbk"
#print(res.text)
main_page = bs(res.text,"html.parser")
alist= main_page.find(attrs={"class":"list"}).find_all("a")
#print(alist)
img_url_list = []
for i in alist:
    #print(i.get("href"))#直接提取href的值，http://www.netbian.com/
    child_url = "http://www.netbian.com/" + str(i.get("href"))
    #print(url)
    child_res = requests.get(child_url)
    child_res.encoding = 'gbk'
    child_page = bs(child_res.text,"html.parser")
    blist = child_page.find("div",attrs={"class":"endpage"})
    try:
        img = blist.find("img")
        #print(img.get("src"))
        img_url = img.get("src")
        img_url_list.append(img_url)#不使用列表的话，字符串报错
        #print(img_url_list)
    except :
        #print(none)
        pass
    num = 4
    for k in img_url_list:
            response = requests.get(k).content
            #print(response.text)
            with open('../照片/{}.jpg'.format(num),"wb") as f:#../表示上一级目录，./表示当前目录
                f.write(response)
                num = num + 1
