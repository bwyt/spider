import requests, execjs
# 获取本次翻译的语种(输入的语种)
url_lang = 'https://fanyi.baidu.com/langdetect'
world = input('要翻译的单词：')
h = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}
d = {
    'query': world
}
response1 = requests.post(url_lang, headers=h, data=d)
# data1 = response1.content.decode()  # --> str
data1 = response1.json()
lan = data1['lan']
# print(lan)

with open('demo.js', 'r') as f:
    js = f.read()
# word = 'hah'
sgin = execjs.compile(js).call('e',world)
# print(sgin)

# 准备翻译的url
url_tra = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'
d = {
    'from': lan,
    'to': 'en' if lan == 'zh' else 'zh',
    'query': world,
    'simple_means_flag': '3',
    'sign': sgin,
    'token': 'ad23d10202c07cd58ac3c0419068e181'
}
response2 = requests.post(url_tra, data=d)
# data2 = response2.json()
# print(response2.json())
print('意思为：',response2.json()['trans_result']['data'][0]['dst'])
