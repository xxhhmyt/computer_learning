import urllib
import requests
from lxml import etree
response = requests.get('https://tieba.baidu.com/p/5475267611').text.encode('utf-8')
#print(response)
select = etree.HTML(response)
image_urls = select.xpath('//img[@class="BDE_Image"]/@src')#ѡȡimg�ڵ㣬����ΪBDE...,��ǰ�ڵ��ֱ���ӽڵ�src
#print(image_url)
offset = 0
for image_url in image_urls:
    #print(image_url)
    image_content = requests.get(image_url).content
    with open('{}.jpg'.format(offset),"wb")as f:
        f.write(image_content)
        offset = offset + 1


