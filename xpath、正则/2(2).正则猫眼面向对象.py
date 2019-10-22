import json

import requests,re

def get_one_page(url):
    # 获取页面html的方法
    header = {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16",
    }
    response = requests.get(url,headers=header)
    return response.text


def parse_one_page(html):
    # 提取数据的方法
    items = re.findall('<dd>.*?<i class="board-index.*?">(.*?)</i>'
                       '.*?class="poster-default".*?<img.*?src="(.*?)"'
                       '.*?<a.*?>(.*?)</a>'
                       '.*?主演：(.*?)</p>'
                       '.*?上映时间：(.*?)</p>'
                       '.*?"integer">(.*?)</i>.*?fraction">(.*?)</i>',html,re.S)
    for item in items:
        dic = {}
        dic['index'] = item[0]  # 排名
        dic['image'] = item[1]  # 图片
        dic['title'] = item[2]  # 名字
        dic['actor'] = item[3].strip()  # 主演
        dic['time'] = item[4]  # 上映时间
        dic['score'] = item[5] + item[6]
        yield dic


def write_to_file(content):
    with open('maoyan.txt','a',encoding='utf-8') as f:
        # print(type(json.dumps(content)))
        f.write(json.dumps(content,ensure_ascii=False)+'\n')



def main():
    for i in range(10):
        url = 'https://maoyan.com/board/4?offset={}'.format(i*10)
        html = get_one_page(url)
        for content in parse_one_page(html):
            write_to_file(content)

main()


















