import random

import requests

# 1.准备代理字典 --> 最多两组键值对 --> http/https
# 键：http/https
# 值：键://账号:密码@IP:post（端口）
# p = {
#     'http': '223.111.131.100:8080',
#     # 'https': ''
# }
#
# url = 'http://httpbin.org/get'
#
# response = requests.get(url, proxies=p)

# print(response.content.decode())


# 随机代理：准备一个代理列表，每一个元素就是一个字典
p_list = [
    {'http': 'http://112.247.181.99:8060'},
    {'http': 'http://139.196.78.83:80'},
    {'http': 'http://223.111.131.100:8080'},
    {'http': 'http://111.29.3.195:80'},
    {'http': 'http://39.137.69.8:8080'},
]
url = 'http://httpbin.org/get'
for i in range(1, 10):
    p = random.choice(p_list)
    try:
        response = requests.get(url, proxies=p, timeout=3)
        print(response.content.decode())
    except Exception as e:
        print('不可使用的代理有：{}'.format(p))

