import requests
url = 'https://www.baidu.com'
response = requests.get(url)

"""
获取请求对象
    print(response.request)
请求头
    print(response.request.headers)
请求url
    print(response.request.url)   
"""
