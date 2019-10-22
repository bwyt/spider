

# http://tieba.baidu.com/f?kw=%E9%87%8D%E5%BA%86%E7%AC%AC%E4%BA%8C%E5%B8%88%E8%8C%83%E5%AD%A6%E9%99%A2&ie=utf-8&pn=50
# http://tieba.baidu.com/f?kw={}&ie=utf-8&pn={}
import os

import requests
from lxml import html

name = input('贴吧名称：')
# 贴吧首页路由
url = 'http://tieba.baidu.com/f?kw={}'.format(name)
response = requests.get(url)
index = response.content
# print(index)
index_inf = html.fromstring(index)
# print(index_inf)
inf = index_inf.xpath('//ul[@id="thread_list"]/li')
# print(inf)

# 贴吧详情页路由
data_list = []
for i in inf:
    temp = {}
    url = 'http://tieba.baidu.com' + i.xpath('.//a[@class="j_th_tit "]/@href')[0]
    data_list.append(url)
# print(data_list)

# 贴吧下一页路由
next_url = 'http:' + index_inf.xpath('//a[text()="下一页>"]/@href')[0]
# print(next_url)
# 图片路径
image_url = []
for url_new in data_list:
    response = requests.get(url_new)
    index = response.content
    index_inf = html.fromstring(index)
    image_url_list = index_inf.xpath('//img[@class="BDE_Image"]/@src')
    # print(image_url_list)
    image_url.append(image_url_list)
print(image_url)
    # print(image_url_list)
if not os.path.exists('image'):
    os.makedirs('image')
for url in image_url:
    for j in url:
        # print(j)
        filename = 'image/' + j.split('/')[-1]
        if filename.endswith('.jpg') or filename.endswith('.png'):
            data = requests.get(j)
            x = data.content
            print(filename)
            with open(filename, 'wb') as f:
                f.write(x)



