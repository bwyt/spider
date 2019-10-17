# import requests
#
# t_name = input('请输入贴吧名：')
# start = int(input('请输入起始页：'))
# end = int(input('请输入结束页：'))
# h = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
# }
#
# # http://tieba.baidu.com/f?kw=%E6%98%93%E7%83%8A%E5%8D%83%E7%8E%BA&ie=utf-8&pn=150
#
# # 准备url列表
# # url模板
# url = 'http://tieba.baidu.com/f?kw='+t_name+'&ie=utf-8&pn={}'
# # url列表：想获取多少页就有多少个url
# url_list = []
# for i in range(start,end+1):
#     url_list.append(url.format((i-1)*50))
# # 遍历url列表发送请求获取响应数据进行保存
# for url in url_list:
#     print(url)
#     # 发送请求
#     response = requests.get(url,headers=h)
#     data = response.content.decode()
#     with open('易烊千玺--{}.html'.format(start),'w',encoding='utf-8') as f:
#         f.write(data)
#     start += 1
#




import requests
t_name = input('请输入贴吧名：')
start = int(input('起始页:'))
end = int(input('结束页:'))
h = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}
url = 'http://tieba.baidu.com/f?kw='+t_name+'&ie=utf-8&pn={}'
url_list = []
for i in range(start,end+1):
    url_list.append(url.format(50*(i-1)))
# print(url_list)
for url in url_list:
    print(url)
    response = requests.get(url,headers=h)
    data = response.content.decode()
    with open('{}_{}.html'.format(t_name,start),'w',encoding='utf-8') as f:
        f.write(data)
    start +=1
