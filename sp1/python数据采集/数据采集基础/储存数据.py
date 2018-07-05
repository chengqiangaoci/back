#媒体文件：只获取URL连接；直接下载源文件
# import requests
# from bs4 import BeautifulSoup
# from urllib.request import urlretrieve

# url = "http://www.pythonscraping.com/"
# response = requests.get(url)
# soup = BeautifulSoup(response.text,"html.parser")
# images = soup.find("a",{"id":"logo"}).find("img").attrs["src"]#get("src")
# urlretrieve(images,"C:/Users/Administrator/Desktop/shujucaiji/" + "logo.jpg")

#下载所有src属性文件
# import os
# from urllib.request import urlretrieve
# from urllib.request import urlopen
# from bs4 import BeautifulSoup

# downloadDirectory = "downloaded"
# baseUrl = "http://pythonscraping.com"

# def getAbsoluteURL(baseUrl, source):
#     if source.startswith("http://www."):
#         url = "http://"+source[11:]
#     elif source.startswith("http://"):
#         url = source
#     elif source.startswith("www."):
#         url = source[4:]
#         url = "http://"+source
#     else:
#         url = baseUrl+"/"+source
#     if baseUrl not in url or ".js" in url:
#         return None
#     return url

# def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory):
#     path = absoluteUrl.replace("www.", "")
#     path = path.replace(baseUrl, "")
#     path = downloadDirectory+path
#     directory = os.path.dirname(path)

#     if not os.path.exists(directory):
#         os.makedirs(directory)

#     return path

# html = urlopen("http://www.pythonscraping.com")
# bsObj = BeautifulSoup(html, "html.parser")
# downloadList = bsObj.findAll(src=True)

# for download in downloadList:
#     fileUrl = getAbsoluteURL(baseUrl, download["src"])
#     if fileUrl is not None:
#         print(fileUrl)
#         urlretrieve(fileUrl, getDownloadPath(baseUrl, fileUrl, downloadDirectory))




#将数据储存在CSV中
# import csv
# #from os import open

# with open("test1.csv","w+") as f:
# 	try:
# 	    writer = csv.writer(f)
# 	    writer.writerow(('number', 'number plus 2', 'number times 2'))
# 	    for i in range(10):
# 	        writer.writerow( (i, i+2, i*2))
# 	finally:
# 	    f.close()

import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://en.wikipedia.org/wiki/Comparison_of_text_editors")
bsObj = BeautifulSoup(html, "html.parser")
table = bsObj.findAll("table",{"class":"wikitable"})[0]
rows = table.findAll("tr")

with open("editors.csv", 'wt', newline='', encoding='utf-8') as f:
	writer = csv.writer(f)#将内容写入这个文件夹
	try:
		for row in rows:
			csvRow = []
			for cell in row.findAll(['td', 'th']):
				csvRow.append(cell.get_text())
			writer.writerow(csvRow)
	finally:
	    f.close()
