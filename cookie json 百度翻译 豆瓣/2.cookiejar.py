# 将cookiejar转换成字典
import requests

response = requests.get('http://www.baidu.com')

cookiejar = response.cookies

dic = requests.utils.dict_from_cookiejar(cookiejar)

print(dic)
cookie = requests.utils.cookiejar_from_dict(dic)
print(cookie)