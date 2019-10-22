import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://mail.qq.com/cgi-bin/loginpage')
time.sleep(2)
driver.switch_to.frame('login_frame')
driver.find_element_by_id('u').send_keys('502046651')

time.sleep(3)
driver.close()




























































