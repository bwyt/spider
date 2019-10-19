import requests

url = 'http://tieba.baidu.com/f?kw=%E5%81%B6%E5%83%8F&red_tag=v0516079351'

x_url = requests.utils.unquote(url)  # 解码

g_x_url = requests.utils.quote(x_url)  # 编码

print(x_url)
print(g_x_url)
