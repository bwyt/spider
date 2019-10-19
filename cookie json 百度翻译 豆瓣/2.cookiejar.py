# 将cookiejar转换成字典
import requests
response = requests.get('http://www.baidu.com')
cookiejar = response.cookies

cookie_dic = requests.utils.dict_from_cookiejar(cookiejar)
cookie_jar = requests.utils.cookiejar_from_dict(cookie_dic)

print(dic)
print(cookie)
