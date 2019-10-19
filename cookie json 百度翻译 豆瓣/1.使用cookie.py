"""
导包
import requests

准备详情页url
url_1 = 'http://www.renren.com/'

发送请求获取响应
    使用cookie
    1.使用请求头携带
    h = {
    'Cookie': 'anonymid=k1vg9kjy-hkszqi; depovince=GW; jebecookies=9f7da129-4f56-4ec7-8694-f05a020066a3|||||; _r01_=1; JSESSIONID=abcbs3vMbr5Kh94VSDC3w; ick_login=79dd572e-dd43-46b7-b936-64be32241e0f'
    }
    response = requests.get(url_1, headers=h)

    2.使用cookies参数携带一个cookie字典
    cookies_str = 'anonymid=k1vg9kjy-hkszqi; depovince=GW; jebecookies=9f7da129-4f56-4ec7-8694-f05a020066a3|||||; _r01_=1; JSESSIONID=abcbs3vMbr5Kh94VSDC3w; ick_login=79dd572e-dd43-46b7-b936-64be32241e0f'
    c = {cookie_str.split('=',maxsplit=1)[0]:cookie_str.split('=',maxsplit=1)[1] for cookie_str in cookies_str.split('; ')}
    response = requests.get(url_1, cookies=c)

    3.使用session对象携带cookie
    session对象 --> requests
    session会自动携带cookie，先进行登录操作

    # 生成session对象
    session = requests.session()
    # 准备登录使用的url
    url = 'http://www.renren.com/PLogin.do'
    session.headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
    }
    # 准备表单数据
    d = {
        'email':'',
        'password':''
    }
    # 先发送登录的请求
    response = session.post(url, data=d)
    # 向详情页发送请求
    response = session.get(url_1)

打印
print(response.content.decode())
"""



