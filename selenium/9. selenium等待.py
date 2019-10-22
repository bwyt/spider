import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://www.baidu.com')

driver.find_element_by_id('kw').send_keys('python')
driver.find_element_by_id('su').click()
# 1. 强制等待
# time.sleep(2)
# 2. 隐式等待: 页面加载完毕就可以执行后面的代码
# driver.implicitly_wait(5)
# driver.find_element_by_link_text('下一页>').click()
# 3. 显示等待: 等待某个规则加载完毕执行后面的代码
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
wait = WebDriverWait(driver, 20, 0.5)
next_bnt = wait.until(EC.presence_of_element_located((By.LINK_TEXT, '下一页>')))
next_bnt.click()

time.sleep(3)

driver.close()















