


# 1. 导包

from pyquery import PyQuery as pq  # as起别名,pq相当于用PyQuery
html = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''

# 2. 将爬取的数据转换为pyquery对象
doc = pq(html)
print(type(doc))

# 3. 需要会css选择器
# 选择所有li
# print(doc('li'))
# 选择类为item-1的标签
# print(doc('.item-1'))

# doc = pq(url='http://www.baidu.com')
# print(type(doc))
# print(doc('head'))

# doc = pq(filename='demo.html')
# print(doc('li'))

# 类,id,标签

# 获取id为container的标签
# print(doc('#container'))
# 获取id为container的标签下的ul标签
# print(doc('#container ul'))
# 获取id为container的标签下的li标签
# print(doc('#container li'))
# 获取class为item-0和active的标签
# print(doc('.item-0.active'))
# print(type(doc('.item-0.active')))

# 获取元素
# find可以获取后代元素
# div = doc('#container')
# print(div.find('li'))
# children可以获取子级元素
# print(div.children('ul'))

# li = doc('.item-1.active')
# parent()获取父级元素
# print(li.parent())
# parents()获取祖先级元素
# print(li.parents())
# siblings()获取兄弟元素
# print(li.siblings())  # 不传入css选择器就是获取所有的兄弟
# print(li.siblings('.item-1'))  # 传入css选择器就是获取特定的兄弟

# 遍历pyquery对象
# lis = doc('li')
# # .items()方法将pyquery转换为可迭代对象
# for li in lis.items():
#     # 获取文本信息.text()
#     print(li.text())
#     print(type(li.text()))
#     # 获取标签属性.attr('属性名')
#     print(li.attr('class'))

# 伪类选择器
lis = doc('li')
print(lis.items())
li = doc('li:first-child')
print(li)
li = doc('li:nth-child(2)')
print(li)








