from selenium import webdriver
import time
driver = webdriver.Firefox()#加载页面
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
time.sleep(3)
print(driver.find_element_by_id("content").text)#加载内容
driver.close()#关闭浏览器，一般不需要关闭，这里仅作掩饰






















