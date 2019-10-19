import requests
url = 'https://www.baidu.com'
response = requests.get(url)

"""
text：获取文本信息 --> 字符串
    print(response.text)

encoding：获取猜测的编码格式 --> ISO-8859-1 --> 希腊格式 
    print(response.encoding)
    response.encoding = 'utf-8'
    print(response.encoding)
    
content：获取返回的二进制信息
    byte = response.content
    print(byte.decode('utf-8'))  # 解码
    
url：获取响应的连接
    print(response.url)
    
headers：获取响应头
    print(response.headers)
    
status_code：获取状态码
    print(response.status_code)
   
获取请求对象
    print(response.request)
"""
