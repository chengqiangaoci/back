#获取汽车直接某个页面的标题、简介、URL、图片。
import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve


#爬取多页
fanwei = range(1,2)
for i in fanwei:
	url = ("http://www.autohome.com.cn/news/%d/#liststart/" %i)
	respose = requests.get(url)
	# print(respose.text)
	respose.encoding = "gbk"
	soup = BeautifulSoup(respose.text,"html.parser")
	x = i*100
	li_list = soup.find(id="auto-channel-lazyload-article").find_all(name="li")
	
	for li in li_list:
		title = li.find("h3")
		if not title:#如果有广告，则可以忽视
			continue
		print("===============")#每个li之间都有分隔符
		summary = li.find("p").text
		print(summary)
		#print(title.text,summary)#标题和简介
		#接下来是URL超链接，与标题和简介的text不同，这里的URL是属性
		#在这里URL在a标签,href属性中
	#url = li.find("a").attrs["href"]
		url = li.find("a").get("href")
	# with open("text.txt","a+") as f:
	# 	f.write(url+"\n")  #自动换行
	#print(title.text,url,summary)#打印标题、简介和URL
	#图片在img标签中，src属性中
		img1 = li.find("img").get("src")
		img2 = img1.replace("www2","www")
		img3 = img1.replace("www3","www")
		img4 = img1.replace("//www","http://www")
	#print(title.text,url,summary,img1)
	#将图片下载到本地的时候，需要再一次请求。
		
		urlretrieve(img4,"C:/Users/Administrator/Desktop/tu/" + "%s.jpg" %x)
		print(str(x) + "下载完成")
		x += 1
	#图片和文件用content，文本使用text
	print("爬取完成")	




