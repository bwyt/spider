import requests
url = 'https://www.baidu.com'
response = requests.get(url)

"""
使用utf进行解码
    print(response.content.decode())

使用gbk进行解码
    print(response.content.decode('gbk'))
"""
print(response.text)
