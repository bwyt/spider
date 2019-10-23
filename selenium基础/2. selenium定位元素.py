import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')

"""
定位页面元素:find_element_by_XXX --> element对象

    通过id定位标签                                  driver.find_element_by_id('kw').send_keys("python")
    通过class属性值定位标签                          driver.find_element_by_class_name('s_ipt').send_keys('haha')
    通过标签name属性的值进行定位                     driver.find_element_by_name("wd").send_keys('hehe')
   
    通过a标签的文本内容定义标签：
        by_link_text 文本内容必须完全一致            driver.find_element_by_link_text('hao123').click()
        by_partial_link_text 文本内容可以部分一致    driver.find_element_by_partial_link_text('hao').click()
    
    通过标签名去获取标签                             ass = driver.find_element_by_tag_name('a')
    通过xpath去定位                                 driver.find_element_by_xpath('//a[@name="tj_trnews"]').click()
    
    
注意点:
    find_element 和find_elements的区别：
				find_element: 返回找到第一个元素,如果没有报错
				find_elements: 返回找到的所有元素列表, 如果没有找到返回空列表
    by_link_text和by_partial_link_text的区别：
				by_link_text: 全部文本都一样
				by_partial_link_text: 包含某个文本
		find_element/ find_elements只能获取元素, 不能获取属性和文本, 要获取属性和文本需要使用get_attribute(属性名) 和.text

"""

# 返回一个element对象的列表
ass = driver.find_elements_by_tag_name('a')
print(ass)


time.sleep(3)
driver.close()


















