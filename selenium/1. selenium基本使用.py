"""
selenium：
    Web的自动化测试工具
    可以直接运行在浏览器上，它支持所有主流的浏览器
安装selenium：
    pip install selenium
安装Google浏览器并配置ChromeDriver：
    点击Google菜单 -> 帮助 -> 关于Google Chrome -> 查看版本号 （版本 71.0.3578.98（正式版本）（64 位））
    下载ChromeDriver：https://chromedriver.storage.googleapis.com/index.html
    对比自己浏览器版本下载相应版本
    解压后把文件放到python的目录下
"""

# 创建浏览器驱动:
from selenium import webdriver
import time
driver = webdriver.Chrome()

"""
各浏览器初始化方法：
    browser = webdriver.Chrome()
    browser = webdriver.Firefox()
    browser = webdriver.Edge()
    browser = webdriver.PhantomJS()
    browser = webdriver.Safari()
"""

# 加载页面: 必须携带协议头
driver.get('https://www.baidu.com')  # dirver 发送完请求后那么他就变为了一个可以操作浏览器的对象
driver.find_element_by_id('kw').send_keys('python')  # .send_keys(文本信息)
time.sleep(2)
driver.find_element_by_id('su').click()  # 定位到按钮,然后点击
"""
查看请求信息：
    driver.page_source: 获取渲染后页面内容
		driver.get_cookies(): 获取cookie信息
		driver.current_url: 当前的URL
"""
print(driver.page_source)
print(driver.current_url)

"""
退出：
    driver.close() 关闭窗口
		driver.quit() 退出浏览器
"""
time.sleep(3)
driver.close()
# driver.quit()









from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
browser = webdriver.Chrome()
try:
  browser.get('https://www.baidu.com')
  input = browser.find_element_by_id('kw')
  input.send_keys('Python')
  input.send_keys(Keys.ENTER)
  wait = WebDriverWait(browser,10)
  wait.until(EC.presence_of_element_located((By.ID,'content_left')))
  print(browser.current_url)
  print(browser.get_cookies())
  print(browser.page_source)
finally:
  browser.close()
  
解释：
可以看到自动弹出浏览器 首先跳转百度 然后搜索框输入Python 接着跳转搜索结果页
搜索结果出来后 控制台输出当前URL Cookies 网页源代码
使用selenium 驱动浏览器加载网页就可以拿到js渲染结果了 不用担心什么加密系统




