#爬取煎蛋上的多页图片
import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
from selenium import webdriver



#以下使用了一个防屏蔽的抬头

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1;WOW64; rv:58.0) Gecko/20100101 Firefox/58.0"}
#1,模仿浏览器
driver = webdriver.Firefox()
#开始遍历页数1-95
fanwei = range(1,2)
for i in fanwei:
#2，URL
	url = ("http://www.jandan.net/ooxx/page-%s#comments" %i)
	# response = requests.get(url,headers=headers).text
#3，通过浏览器读取URL
	response = driver.get(url)

	#print(response.text)
	# response.encoding = "gbk"
#4，对象化
	soup = BeautifulSoup(driver.page_source,"html.parser")
	x = i*100
	try:
		li_list1 = soup.find(class_="commentlist").find_all(name="li")
		#print(li_list1)
		for li_list in li_list1:
			if not li_list:
				continue
			#print(li_list)
			tupian = li_list.find("img")#一定要注意这里不能find str，而是img定位到URL
			#print(tupian)
			if str("jpg") in str(tupian):
				tupian1 = tupian.get("src")
			else:
				pass#如果想获取gif图片，这里可以改为tupian1 = tupian.get("org_src")
			#print(tupian1)
			urlretrieve(tupian1,"C:/Users/Administrator/Desktop/jandan/" + "%s.jpg" %x)
			print(str(x)+"下载完成")
			print("=================")
			x += 1
	except Exception:
		continue
print("爬取完成")
