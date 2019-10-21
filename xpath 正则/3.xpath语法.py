"""
lxml是一款高性能的 Python HTML/XML解析器，我们可以利用XPath，来快速的定位特定元素以及获取节点信息

	安装:pip install lxml
	导包:from lxml import html
	转换element对象:html.fromstring(str)
	使用xpath语法提取数据.xpath(xpath语法)

XPATH提取数据的原则:
	先分组, 获取包含数据的标签列表
	遍历标签列表, 提取数据.

"""


"""
1. 准备html字符串
    text =''

2. 将str --> element对象
    element = html.fromstring(text)

3. 获取标签，xpath语法会返回element对象

    路径：
        绝对路径：/
        不看层级获取标签：//
        .   当前节点
        ..  父节点              --> element.xpath('//li/a/..)
        @属性名    获取属性值   --> element.xpath('//li/a/@href')
        text()  获取文本内容    --> element.xpath('//li//text()')

        获取属性：href，src
        定位属性：id，class

    过滤（定位）：
        [1]：获取第一个标签[索引] --> xpath索引从1开始
        [last()]：获取最后一个
        [last()-1]：获取倒数第二个
        [m]|[n]：获取m或n
        [position()>n]：获取位置大于n的标签
        [text()='值']：获取指定文本的标签 --> 全等
        [contains(text(),'文本信息')]：获取文本内容 --> 模糊查询
        [@属性名='属性值']：获取指定属性     --> element.xpath('//li[@class="item-0"]')

    通配符
        *： 任意节点
        @*：任意属性

res = element.xpath('')
print(res)
"""

from lxml import html
text='''
<div>
    <ul>
        <li class="item-0"><a href="link1.html"><span>first item</span></a><>
        <li class="item-1"><a href="link2.html">second item</a><>
        <li class="item-inactive"><a href="link3.html">third item</a><>
        <li class="item-1"><a href="link4.html">fourth item</a><>
        <li class="item-0"><a href="link5.html">fifth item</a>
    </ul>
</div>
'''
element = html.fromstring(text)
# print(html.tostring(element))  --> 自动补全
# 返回所有span节点
ret_2 = element.xpath('//span')
print(ret_2)
# 返回所有li下的a节点
ret_3 = element.xpath('//li/a')
print(ret_3)
# 返回span的父节点
ret_4 = element.xpath('//span/..')
print(ret_4)
# 选取class为item-0 的li节点
ret_5 = element.xpath('//li[@class="item-0"]')
print(ret_5)
# 获取li节点中的文本
ret_6 = element.xpath('//li//text()')
print(ret_6)
# 获取li节点下所有a节点的href属性
ret_7 = element.xpath('//li/a/@href')
print(ret_7)



