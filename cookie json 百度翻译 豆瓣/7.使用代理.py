"""
使用代理：让服务器认为是不同的客户端在发送请求
	     防止我们的真实地址被泄露,防止被追究责任
         
         正向代理保护客户端
	     反向代理保护服务器
         
代理分类
		透明代理:知道真实IP知道使用代理
		匿名代理:知道使用代理但是不知道真实IP
		高匿代理:既不知道使用代理有不知道真实IP
"""

import random
import requests

"""
准备代理字典 --> 最多两组键值对 --> http/https
键：http/https
值：键://账号:密码@IP:post（端口）
"""
p = {
    'http': '223.111.131.100:8080',
    # 'https': ''
}
url = 'http://httpbin.org/get'
response = requests.get(url, proxies=p)
print(response.content.decode())


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
    p = random.choice(p_list)  # 随机取一个代理IP
    try:
        response = requests.get(url, proxies=p, timeout=3)
        print(response.content.decode())  # 使用代理IP发送请求
    except Exception as e:
        print('不可使用的代理有：{}'.format(p))
