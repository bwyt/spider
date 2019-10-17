import requests
url = 'http://httpbin.org/post'
h = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}

# 请求体
d = {
    'haha':'hah',
    '哈哈':'heieh'
}

# 发送post请求
response = requests.post(url,headers=h,data=d)

# 转换json格式的数据
print(response.json())