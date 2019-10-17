# """
# 实例化
# run发放
# 获取url列表
# 获取数据
# 保存数据
# """
# import requests
#
#
# class Me:
#     # 实例化
#     def __init__(self, t_name, start, end):
#         self.t_name = t_name
#         self.start = start
#         self.end = end
#         self.h = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}
#         self.url = 'http://tieba.baidu.com/f?kw='+self.t_name+'&ie=utf-8&pn={}'
#
#     # 获取url列表
#     def get_url_list(self):
#         url_list = []
#         for i in range(self.start, self.end+1):
#             url_list.append(self.url.format(50*(i-1)))
#         return url_list
#
#     # 获取数据
#     def get_data(self, url_list):
#         for url in url_list:
#             response = requests.get(url, headers=self.h)
#             data = response.content.decode()
#             self.save_data(data)
#             self.start += 1
#
#     # 保存数据
#     def save_data(self, data):
#         with open(self.t_name+'-{}.html'.format(self.start), 'w', encoding='utf-8') as f:
#             f.write(data)
#
#     # run发放
#     def run(self):
#         url_list = self.get_url_list()
#         self.get_data(url_list)
#
#
# if __name__ == '__main__':
#     a = Me('1', 1, 2)
#     a.run()
#
#

import requests
url = 'http://tieba.baidu.com/f?kw={}&ie=utf-8&pn={}'
name = input('贴吧名：')
start = int(input('开始：'))
end = int(input('结束：'))
h = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}
url_list = []
for i in range(start,end+1):
    url_list.append(url.format(name, 50*(i-1)))
print(url_list)
for url in url_list:
    print(url)
    response = requests.get(url,headers=h)
    data = response.content.decode()
    with open('{}-{}.html'.format(name,start), 'w', encoding='utf-8') as f :
        f.write(data)
        start+=1

