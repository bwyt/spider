from selenium import webdriver
import time


driver = webdriver.Chrome()

driver.get('https://www.baidu.com')
# dirver 发送完请求后那么他就变为了一个可以操作浏览器的对象
# find_element_by_id通过标签的id属性值定位到此标签
# .send_keys(文本信息)
driver.find_element_by_id('kw').send_keys('python')
# 定位到按钮,然后点击
time.sleep(2)
driver.find_element_by_id('su').click()

print(driver.page_source)
print(driver.current_url)
time.sleep(3)
driver.close()
# driver.quit()














