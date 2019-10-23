"""
发送请求
    1.1生成driver对象
    2.1窗口最大化
    2.2下拉滚动条（保证每个位置都刷新）
    3.获取所有li标签列表
    遍历li标签列表提取图片的连接以及主播的名字
    保存图片
翻页
"""
import time
import requests
from selenium import webdriver
# 生成driver对象
driver = webdriver.Chrome()
# 先将窗口最大化
driver.maximize_window()
# 再到达指定路由
driver.get('https://www.douyu.com/g_hpjy')
while True:
    time.sleep(2)
    # 下拉滚动条（保证每个位置都刷新）
    for i in range(2):
        driver.execute_script('window.scrollTo(0,{})'.format(i*500))
        time.sleep(1)
    # 获取所有图片的li标签列表
    lis = driver.find_elements_by_xpath('//ul[@class="layout-Cover-list"]/li')
    # 遍历li标签列表提取图片的连接以及主播的名字
    for li in lis:
        img_url = li.find_element_by_xpath('.//a[1]/div/div[1]/img').get_attribute('src')
        peo_url = li.find_element_by_xpath('.//h2').text
        # 保存图片
        response = requests.get(img_url)
        data = response.content
        file = 'images/' + peo_url + '.webp'
        with open(file, 'wb') as f:
            f.write(data)
    try:
        # 翻页
        next_url = driver.find_element_by_xpath('//li[@class=" dy-Pagination-next"]').click()
    except Exception as e:
        print(e)
        break
time.sleep(5)
driver.close()


