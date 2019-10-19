import requests, json

# 准备url
url = 'https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=200&page_start=0'

h = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}
# 发送请求获取响应数据
response = requests.get(url, headers=h)

# 提取数据
data = response.json()
list = data['subjects']

with open('豆瓣.json', 'w', encoding='utf-8') as f:
    for i in list:
        dic = {}
        dic['title'] = i['title']
        dic['rate'] = i['rate']
        dic['cover'] = i['cover']
        json.dump(dic, f, ensure_ascii=False)
        f.write(',\n')
















