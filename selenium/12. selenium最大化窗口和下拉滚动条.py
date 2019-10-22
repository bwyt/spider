import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://www.baidu.com/s?wd=python')
time.sleep(2)
driver.execute_script('window.scrollTo(0,800)')


time.sleep(3)
driver.close()




























































