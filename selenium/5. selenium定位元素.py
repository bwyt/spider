import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://www.baidu.com')

# 1. 通过id定位标签
# driver.find_element_by_id('kw').send_keys("python")
# 2. 通过类属性值定位标签
# driver.find_element_by_class_name('s_ipt').send_keys('haha')
# 3. 通过标签name属性的值进行定位
# driver.find_element_by_name("wd").send_keys('hehe')
# 4. 通过a标签的文本内容定义标签
# by_link_text 文本内容必须完全一致
# driver.find_element_by_link_text('hao123').click()
# by_partial_link_text 文本内容可以部分一致
# driver.find_element_by_partial_link_text('hao').click()

# inp = driver.find_element_by_id('kw')
# find_element_by_XXX 会返回一个element对象
#  5. 通过标签名去获取标签
# ass = driver.find_element_by_tag_name('a')
# print(ass)
# 6. 通过xpath去定位
# driver.find_element_by_xpath('//a[@name="tj_trnews"]').click()

# 返回一个element对象的列表
ass = driver.find_elements_by_tag_name('a')
print(ass)


time.sleep(3)
driver.close()


















