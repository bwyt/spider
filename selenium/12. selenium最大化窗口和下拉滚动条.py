import time
from selenium import webdriver

driver = webdriver.Chrome()

# 窗口最大化
driver.maximize_window()

driver.get('https://www.baidu.com/s?wd=python')
time.sleep(2)
# 下拉滚动条 -->  execute_script('window.scrollTo(横,纵)')
driver.execute_script('window.scrollTo(0,800)')

time.sleep(3)
driver.close()

