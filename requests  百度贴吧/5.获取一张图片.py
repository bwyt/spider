"""
导包
准备图片的url
发送请求
图片 --> 二进制
将二进制写入文件
"""

import requests
url = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1571293794898&di=80d2a27a79115322aedb10038c1e693e&imgtype=0&src=http%3A%2F%2Fpic1.win4000.com%2Fwallpaper%2F2018-04-02%2F5ac192d94aca9.jpg"
response = requests.get(url)
b = response.content
with open('易烊千玺.jpg', 'wb') as f:
    f.write(b)


