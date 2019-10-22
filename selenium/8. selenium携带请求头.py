from selenium import webdriver
import time

# 1. 获取chrome浏览器的设置对象
opt = webdriver.ChromeOptions()
# 2. 对设置对象中的headless属性进行设置
opt.headless = True
# 3. 在创建驱动对象的时候把设置对象传入
# 添加请求头
opt.add_argument('user-agent="XXXX"')
# 使用代理
opt.add_argument('--proxy-server=http://39.137.107.98:80')

dirver = webdriver.Chrome(options=opt)

dirver.get('http://httpbin.org/get')

# 先分组在获取数据
print(dirver.page_source)


time.sleep(3)
dirver.close()
























