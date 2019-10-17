import requests
t_name = input('请输入贴吧名：')
start = int(input('起始页:'))
end = int(input('结束页:'))
h = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}
# url模板
# url = 'http://tieba.baidu.com/f?kw='+t_name+'&ie=utf-8&pn={}'
url = 'http://tieba.baidu.com/f?kw={}&ie=utf-8&pn={}'
# 准备url列表：想获取多少页就有多少个url
url_list = []
for i in range(start,end+1):
    url_list.append(url.format(50*(i-1)))
# print(url_list)
# 遍历url列表发送请求获取响应数据进行保存
for url in url_list:
    print(url)
     # 发送请求
    response = requests.get(url,headers=h)
    data = response.content.decode()
#     with open(t_name+'-{}.html'.format(start),'w',encoding='utf-8') as f:
    with open('{}_{}.html'.format(t_name,start),'w',encoding='utf-8') as f:
        f.write(data)
    start +=1
