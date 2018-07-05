# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import re

#zh_pattern = re.compile(u'[\u4e00-\u9fa5]+') #检验是否是中文
for i in range(1,2):
	url = "http://www.lesmao.cc/plugin.php?id=group&page=%s" % i
	
	response = requests.get(url).text
	soup = BeautifulSoup(response,"html.parser")
	tupian_list = soup.find("div",{"id":"index-pic"}).find_all("div",{"class":"group"})
	#print(tupian_list)
	for tupian in tupian_list:
		miaoshu = tupian.find("img").get("alt")
		lianjie = tupian.find("img").get("src")
		urlretrieve(lianjie,"C:/Users/Administrator/Desktop/jandan/" + "%s.jpg" %(miaoshu))
		# x += 1
		print(str(miaoshu),"下载完成")
		print("================")
print("完成")