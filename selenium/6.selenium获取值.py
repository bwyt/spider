from selenium import webdriver
import time

dirver = webdriver.Chrome()

dirver.get('https://www.baidu.com')

ass = dirver.find_element_by_link_text('hao123')
# 标签属性的值
# print(ass.get_attribute('href'))
# print(type(ass.get_attribute('href')))
# # 获取文本信息
# print(ass.text)
# print(type(ass.text))

# 先分组在获取数据
div = dirver.find_element_by_id('u1')
a_s = div.find_elements_by_tag_name('a')
for a in a_s:
    print(a.text)
    print(a.get_attribute('href'))


time.sleep(3)
dirver.close()
























