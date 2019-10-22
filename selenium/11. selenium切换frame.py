import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://mail.qq.com/cgi-bin/loginpage')
time.sleep(2)

# frame切换 --> switch_to.frame('name属性值')
driver.switch_to.frame('login_frame')

"""
切换window窗口
		driver.window_handles -->  获取driver中所有窗口的名称
		driver.switch_to.window(窗口名称)  -->  把当前driver切换到指定窗口
"""

# send_keys()  -->  向输入框中输入内容
driver.find_element_by_id('u').send_keys('502046651')

time.sleep(3)
driver.close()


