"""
实例化
run发放
获取url列表
获取数据
保存数据
"""
import requests


class Me:
    # 实例化
    def __init__(self, t_name, start, end):
        self.t_name = t_name
        self.start = start
        self.end = end
        self.h = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}
        self.url = 'http://tieba.baidu.com/f?kw='+self.t_name+'&ie=utf-8&pn={}'

    # 获取url列表
    def get_url_list(self):
        url_list = []
        for i in range(self.start, self.end+1):
            url_list.append(self.url.format(50*(i-1)))
        return url_list

    # 获取数据
    def get_data(self, url_list):
        page = self.start
        # 遍历列表发送请求获取响应数据
        for url in url_list:
            response = requests.get(url, headers=self.h)
            data = response.content.decode()
            # 调用保存数据的方法
            self.save_data(data)
            # self.start += 1
            page += 1


    # 保存数据
    def save_data(self, data, page):
        with open(self.t_name+'-{}.html'.format(page), 'w', encoding='utf-8') as f:
            f.write(data)

    # run发放
    def run(self):
        # 获取url列表
        url_list = self.get_url_list()
        # 遍历url_list方法请求
        self.get_data(url_list)


if __name__ == '__main__':
    a = Me('1', 1, 2)
    a.run()



