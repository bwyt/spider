from selenium import webdriver
import time

# 1. 获取chrome浏览器的设置对象
opt = webdriver.ChromeOptions()
# 2. 对设置对象中的headless属性进行设置
opt.headless = True
# 3. 在创建驱动对象的时候把设置对象传入
dirver = webdriver.Chrome(options=opt)

dirver.get('https://www.baidu.com')

# 先分组在获取数据
div = dirver.find_element_by_id('u1')
a_s = div.find_elements_by_tag_name('a')
for a in a_s:
    print(a.text)
    print(a.get_attribute('href'))


time.sleep(3)
dirver.close()
























