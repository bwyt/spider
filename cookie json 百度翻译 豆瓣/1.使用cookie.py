import requests  # 导包

url_1 = 'http://www.renren.com/972513153/newsfeed/photo'  # 准备详情页url_1

"""
发送请求获取响应    

    1.使用headers携带cookie
    
    h = {
    'Cookie': 'anonymid=k1vg9kjy-hkszqi; depovince=GW; jebecookies=9f7da129-4f56-4ec7-8694-f05a020066a3|||||; _r01_=1; JSESSIONID=abcbs3vMbr5Kh94VSDC3w; ick_login=79dd572e-dd43-46b7-b936-64be32241e0f'
    }
    response = requests.get(url_1, headers=h)



    2.使用cookies参数携带一个cookie字典
      把cookie放在字典内部,使用cookies参数接受
      
    cookies_str = 'anonymid=k1vg9kjy-hkszqi; depovince=GW; jebecookies=9f7da129-4f56-4ec7-8694-f05a020066a3|||||; _r01_=1; JSESSIONID=abcbs3vMbr5Kh94VSDC3w; ick_login=79dd572e-dd43-46b7-b936-64be32241e0f'
    c = {cookie_str.split('=',maxsplit=1)[0]:cookie_str.split('=',maxsplit=1)[1] for cookie_str in cookies_str.split('; ')}
    response = requests.get(url_1, cookies=c)



    3.使用requests提供的session对象携带cookie
      session会自动记录请求获取的cookie下载请求自动带着cookie
        session对象 --> requests
        session会自动携带cookie，先进行登录操作
        
    session = requests.session()  # 生成session对象
    url = 'http://www.renren.com/PLogin.do'  # 准备登录使用的url
    session.headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
    }
    # 准备表单数据
    d = {
        'email':'账号名',
        'password':'密码'
    }
    response = session.post(url, data=d)  # # 先发送登录的请求
    response = session.get(url_1)  # # 向详情页发送请求
"""

print(response.content.decode())  # 打印



