import requests
from bs4 import BeautifulSoup

#基本操作
# url = "http://www.pythonscraping.com/pages/page1.html"
# response = requests.get(url)
# soup = BeautifulSoup(response.text,"html.parser")
# print(soup)


# url = "http://www.pythonscraping.com/pages/warandpeace.html"
# response = requests.get(url)
# soup = BeautifulSoup(response.text,"html.parser")
# namelist = soup.find_all("span",{"class":"green"})
# print(namelist.text)



# url = "https://en.wikipedia.org/wiki/Kevin_Bacon"
# response = requests.get(url)
# soup = BeautifulSoup(response.text,"html.parser")
# for link in soup.find_all("a"): #a标签
# 	if "href" in link.attrs:
# 		print(link.attrs["href"])


#子标签与后代标签
# url = "http://www.pythonscraping.com/pages/page3.html"
# response = requests.get(url)
# soup = BeautifulSoup(response.text,"html.parser")
# testlist = soup.find_all("table",{"id":"giftList"})
# for list in testlist:
# 	print(list.get_text())#只获取文本，没有标签


#正则表达式
import re
url = "http://www.pythonscraping.com/pages/page3.html"
response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")
images = soup.find_all("img",{"src":re.compile("\.\.\/img\/gifts\/img.*\.jpg")})
for image in images:
	print(image["src"])







