# 正则：从字符串中提取数据，贪婪
# re.方法('正则表达式'， '需要提取的字符串')

# 单字符操作
"""
.   匹配除了\n以外所有的字符
    匹配\n --> re.S
[]  枚举，匹配[]内有的字符
\d  数字
\D  非数字
\s  空白字符 --> 空格 TAB \r \t \n
\S  非空白字符
\w  单词字符：python中：字符数字下划线汉字
\W  非单词字符   -->  [^\w]
"""
# 多字符操作
import requests

"""
*       [0,+∞)
+       [1,+∞)
?       [0,1]
{n}     n次
{m,n}   [m,n] --> 默认取n，当取不了n，再取m
{n,}    [n,+∞)

"""
import re
# # --> findall：返回一个列表
# ret1 = re.findall('\w+','python6班\npython7班')
# ret2 = re.findall('\w*','python6班\npython7班')
# ret3 = re.findall('\w?','python6班\npython7班')
# ret4 = re.findall('\w{3}','python6班\npython7班')
# ret5 = re.findall('\w{2,3}','python6班\npython7班')
#
# print(ret1)
# print(ret2)
# print(ret3)
# print(ret4)
# print(ret5)



"""
match   从头开始匹配，成功 --> match对象，失败 --> None
search  全局匹配，返回第一次匹配成功的结果 --> match对象
findall 全局匹配，返回所有匹配成功的结果的列表
sub('正则','替换后','替换前')   替换字符串   
"""

"""
()      分组,匹配括号里面的
re.I    忽略大小写
re.S    可以匹配换行



"""




# ret_ma = re.match('\w+','python6班\n')
# ret_ma = re.match('\w*','python6班\n')
# ret_ma = re.match('\w*','\npython6班\n')
# ret_ma = re.match('.*','python6班\n')
# ret_ma = re.match('.*','python6班\n',re.S)
# ret_ma = re.search('\w+','\npython6班\n')
# ret_ma = re.search('\w*','\npython6班\n')
# ret_ma = re.findall('\w*','\npython6班\n')
# ret_ma = re.findall('\w+','\npython6班\n')
# ret_ma = re.findall('\d+','\npython6班\npython7班\npython8班\n')
# ret_ma = re.findall('python(\w+)班','\npython6班\npython七班\npython8班\n')
# ret_ma = re.sub('\d+','yi','python6班,python5班\npython7班')
#
#
# print(ret_ma)
# print(ret_ma.group())



# s = '"title": "致命女人 第一季", "rate": "9.3", "cover": "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2566967861.jpg"'
# ret = re.findall('.*?"cover": "(.*?)"',s)
# print(ret)

url = 'https://www.baidu.com/'
response = requests.get(url)
pro = response.content.decode()
# print(pro)
inf = re.findall('<a href=(.*?)name.*?class=mnav>(.*?)</a>', pro)
for i in inf:
    dic = {}
    dic['网址'] = i[0]
    dic['name'] = i[1]
    print(dic)
# print(inf)



# compile：预编译，把正则表达式编译为2进制形式,提高匹配的速度
# regex = re.compile('正则')
# # ret = regex.findall('字符串')
# # print(ret)


# 转义符
# print('\n')
# print(r'\n')
# print('\\n')
# print(len('\n'))
# print(len(r'\n'))
# print(len('\\n'))
