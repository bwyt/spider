import requests


"""
1.通过get请求携带请求头 --> User-Agent
    url = 'https://www.baidu.com/'
    准备请求头
    h = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
    }
    # 网页 --> 检查 --> NetWork --> 刷新 --> Headers --> User-Agent
    # 百度搜索User-Agent
    
    携带请求头
    response = requests.get(url,headers=h)
    print(response.request.headers)
    
2.get请求携带参数
    1.手动拼接URL
        url = 'https://www.baidu.com/s?wd={}'
         h = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
        }
        s = input('请输入要搜索的关键字：')
        url = url.format(s)
        response = requests.get(url,headers=h)
        print(response.content.decode())
        
    2.使用params参数携带查询字符串参数
        url = 'https://www.baidu.com/s'
        h = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
        }
        # {'参数名':'参数值'}
        p = {
        'wd':'python'
        }
        response = requests.get(url,headers=h,params=p)
        print(response.content.decode())
    
"""

# url = 'https://www.baidu.com'
# h = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
# }
# response = requests.get(url,headers=h)
# print(response.request.headers)

# url = 'https://www.baidu.com/s'
# h = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
# }
# p = {
#     'wd':'python'
# }
# response = requests.get(url,headers=h,params=p)
# print(response.content.decode())

url = 'https://www.baidu.com/s?wd={}'
h = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}
s = input('查询字段:')
url = url.format(s)
print(url)
response = requests.get(url,headers=h)
print(response.content.decode())

