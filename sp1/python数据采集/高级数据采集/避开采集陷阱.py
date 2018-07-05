#修改请求头
# import requests
# from bs4 import BeautifulSoup

# session = requests.Session()
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1;WOW64; rv:58.0) Gecko/20100101 Firefox/58.0"}
# url = "https://www.whatismybrowser.com/detect/what-http-headers-is-my-browser-sending"
# req = session.get(url, headers=headers)
# bsObj = BeautifulSoup(req.text, "lxml")
# print(bsObj.find("table",{"class":"table-striped"}).get_text)



#处理cookies
# from selenium import webdriver
# driver = webdriver.PhantomJS(executable_path='<Path to Phantom JS>')
# driver.get("http://pythonscraping.com")
# driver.implicitly_wait(1)
# print(driver.get_cookies())

# savedCookies = driver.get_cookies()

# driver2 = webdriver.PhantomJS(executable_path='<Path to Phantom JS>')
# driver2.get("http://pythonscraping.com")
# driver2.delete_all_cookies()
# for cookie in savedCookies:
#     driver2.add_cookie(cookie)

# driver2.get("http://pythonscraping.com")
# driver.implicitly_wait(1)
# print(driver2.get_cookies())




#休眠
time.sleep(3)