import requests
url = 'https://www.baidu.com'
response = requests.get(url)

"""
使用utf进行解码
    print(response.content.decode())

使用gbk进行解码  # http://www.people.com.cn/
    print(response.content.decode('gbk'))
    
使用response.text属性
"""

print(response.text)
