import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://www.baidu.com')

driver.find_element_by_id('kw').send_keys('jd')
driver.find_element_by_id('su').click()
time.sleep(2)
driver.find_element_by_partial_link_text('京东').click()


driver.switch_to.window(driver.window_handles[1])
time.sleep(1)
print(driver.title)

time.sleep(1000)
driver.close()




























































