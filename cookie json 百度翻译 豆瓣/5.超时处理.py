import requests
url = 'http://www.facebook.com'
# 参数：timeout(数字)，单位为秒
# 超过指定时间，没返回数据，抛出timeout异常
try:
    response = requests.get(url, timeout=1)
    print(response.content.decode())
except Exception as e:
    print('无法访问的网站有：{}'.format(url))