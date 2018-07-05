import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
#from selenium import webdriver
#driver = webdriver.Firefox()

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1;WOW64; rv:58.0) Gecko/20100101 Firefox/58.0"}

url = "https://www.814aa.com/htm/girl10/2421.htm"
#response = driver.get(url)
response = requests.get(url,headers=headers).text
soup = BeautifulSoup(response,"html.parser")
x = 1
tupian_list = soup.find(class_="picContent").find_all("img")
for i in tupian_list:
	tupian = i.get("src")
	# print(tupian)
	urlretrieve(tupian,"C:/Users/Administrator/Desktop/jandan/" + '%s.jpg' %x)
	print(str(x) + "下载完成")
	x += 1
print("爬取完成")