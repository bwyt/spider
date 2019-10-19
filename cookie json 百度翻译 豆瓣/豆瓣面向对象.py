"""
实例化
获取url列表
获取数据
保存数据
run发放
"""

import requests,json


class Me:
    def __init__(self):
        self.h = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}
        self.url = 'https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=200&page_start=0'

    def get_data(self):
        response = requests.get(self.url,headers=self.h)
        data = response.json()
        list = data['subjects']
        return list

    # 准备dic
    def pre_dic(self,list):
        data_list = []
        for i in list:
            dic = {}
            dic['title'] = i['title']
            dic['rate'] = i['rate']
            dic['cover'] = i['cover']
            data_list.append(dic)
        return data_list

    def save_data(self, data_list):
        with open('豆瓣1.json', 'w', encoding='utf-8') as f:
            json.dump(data_list, f, ensure_ascii=False)
            f.write(',\n')

    def run(self):
        list = self.get_data()
        data_list = self.pre_dic(list)
        self.save_data(data_list)


if __name__ == '__main__':
    p = Me()
    p.run()
