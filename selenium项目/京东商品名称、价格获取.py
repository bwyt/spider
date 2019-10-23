import json
import time
from selenium import webdriver

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
driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(1)
driver.get('https://list.jd.com/list.html?cat=9987,653,655&ev=exbrand%5F12669&sort=sort_rank_asc&trans=1&JL=3_%E5%93%81%E7%89%8C_%E9%AD%85%E6%97%8F%EF%BC%88MEIZU%EF%BC%89#J_crumbsBar')
while True:
    time.sleep(1)
    for i in range(16):
        driver.execute_script('window.scrollTo(0,{})'.format(i * 500))
        time.sleep(1)
    lis = driver.find_elements_by_xpath('//ul[@class="gl-warp clearfix"]/li')
    with open('京东.txt', 'a', encoding='utf-8') as f:
        for li in lis:
            img_url = li.find_element_by_xpath('./div/div[1]/a/img').get_attribute('src')
            price = li.find_element_by_xpath('.//strong[@class="J_price"]').text
            buyers = li.find_element_by_xpath('./div/div[5]/strong').text
            name = li.find_element_by_xpath('./div/div[4]//em').text

            dic = {}
            dic['name'] = name
            dic['price'] = price
            dic['buyers'] = buyers
            json.dump(dic, f, ensure_ascii=False)
            f.write(',\n')
    try:
        next_url = driver.find_element_by_xpath('//a[@class="pn-next"]').click()
    except Exception as e:
        print(e)
        break

time.sleep(1)
driver.close()



