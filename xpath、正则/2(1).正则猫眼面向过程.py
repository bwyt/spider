
# https://maoyan.com/board/4?offset=10
import json

import requests, re
# 获取页面html
# 分析一页数据

# url = 'https://maoyan.com/board/4?offset=0'
url = 'https://maoyan.com/board/4?offset={}'
h = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}
url_list = []
for i in range(1, 11):
    url_list.append(url.format((i-1)*10))
for url in url_list:
    response = requests.get(url, headers=h)
    html = response.content.decode()
    print(html)
# 排名、图片、名称、主演、上映时间、评分
    inf = re.findall('<dd>.*?<i class="board-index.*?">(.*?)</i>'
                     '.*?<img data-src="(.*?)".*?'
                     '<p class="name">.*?>(.*?)</a></p>'
                     '.*?<p class="star">.*?：(.*?)</p>'
                     '.*?<p class="releasetime">.*?：(.*?)</p>'
                     '.*?<i class="integer">(.*?)</i><i class="fraction">(.*?)</i>'
                     , html, re.S)

    with open('maoyan.txt', 'a', encoding='utf-8') as f:
        for i in inf:
            # print(i)
            dic = {}
            dic['index'] = i[0]
            dic['image'] = i[1]
            dic['title'] = i[2]
            dic['author'] = i[3].strip()
            dic['time'] = i[4]
            dic['score'] = i[5]+i[6]
            json.dump(dic, f, ensure_ascii=False)
            f.write(',\n')
