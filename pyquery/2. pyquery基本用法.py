"""
pyquery：是一个强大的网页解析工具它提供了和jQuery类似的语法来解析HTML文档，支持CSS选择器,使用非常方便
# 安装
pip install pyquery
"""

# 导包
from pyquery import PyQuery as pq  # as起别名,pq相当于用PyQuery

"""
初始化：
    1. 字符串初始化
        doc = pq(html)
    2. URL初始化
        doc = pq(url='http://www.baidu.com')
        print(doc('head'))
    3. 文件初始化
        doc = pq(filename='demo.html')
        print(doc('li'))
"""

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

# 将爬取的数据转换为pyquery对象
doc = pq(html)

"""
css选择器：
    1.  #id 
        获取id为container的标签              print(doc('#container'))
        获取id为container的标签下的ul标签     print(doc('#container ul'))
        获取id为container的标签下的li标签     print(doc('#container li'))
        获取class为item-0和active的标签       print(doc('.item-0.active'))
        
	2.  .类属性值
        选择类为item-1的标签                  print(doc('.item-1'))
        
	3.  标签名
        选择所有li                            print(doc('li'))
"""

"""
查询子元素：
    find()，获取所有后代元素                 div = doc('#container')
                                           print(div.find('li'))
                                        
    children()，获取子级元素                print(div.children('ul'))
    
    parent()，父节点：获取父级元素           li = doc('.item-1.active')
                                           print(li.parent())
                                           
    parents()，祖先节点：获取祖先级元素      print(li.parents())
    
    siblings()，兄弟节点：获取兄弟元素       print(li.siblings())           不传入css选择器就是获取所有的兄弟
                                           print(li.siblings('.item-1'))  传入css选择器就是获取特定的兄弟
"""

# 遍历pyquery对象
lis = doc('li')
# .items()方法将pyquery转换为可迭代对象
for li in lis.items():
    # 获取文本信息.text()
    print(li.text())
    # 获取标签属性.attr('属性名')
    print(li.attr('class'))
    # 获取html
	print(li.html())
    

    
lis = doc('li')
print(lis.items())
"""
伪类选择器：
    li = doc('li:first-child')      第一个标签
	li = doc('li:last-child')		最后一个标签
	li = doc('li:nth-child(2)')	    获取第二个标签
	li = doc('li:gt(2)')	        获取序号大于2标签
	li = doc('li:nth-child(2n)')	获取偶数标签标签
	li = doc('li:contains(second)')	包涵second文本的标签
"""
print(li)

