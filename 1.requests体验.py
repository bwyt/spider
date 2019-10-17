"""
requests 使用三步骤
1. 导包
import requests
2. 发送请求
    准备url
    url = 'https://www.baidu.com'
    向url发送请求获取响应对象(发送什么，请求什么)
    response = requests.get(url)
3. 提取数据
print(response.text)
"""
# import requests
# url = 'https://www.baidu.com'
# response = requests.get(url)
# print(response.text)

# import requests
# url = 'http://www.people.com.cn'
# response = requests.get(url)
# response.encoding = 'gbk'
# print(response.text)

import requests
url = 'https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=易烊千玺&step_word=&hs=0&pn=4&spn=0&di=49940&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=0&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=undefined&cs=1101079303%2C1307471305&os=218429534%2C2671575176&simid=18351592%2C853187396&adpicid=0&lpn=0&ln=1330&fr=&fmq=1571283358818_R&fm=&ic=undefined&s=undefined&hd=undefined&latest=undefined&copyright=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=&objurl=http%3A%2F%2Fpic1.win4000.com%2Fwallpaper%2F2018-04-02%2F5ac192d94aca9.jpg&fromurl=ippr_z2C%24qAzdH3FAzdH3Fooo_z%26e3Botg9aaa_z%26e3Bv54AzdH3Fowssrwrj6_1jpwts_8990na_m_z%26e3Bip4s&gsm=&rpstart=0&rpnum=0&islist=&querylist=&force=undefined'
response = requests.get(url)
print(response.content)
print(response.text)

