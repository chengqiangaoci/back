#爬虫基本操作、获取汽车直接某个标题内容
import requests
from bs4 import BeautifulSoup
respose = requests.get("http://www.autohome.com.cn/news/")
respose.encoding = "gbk"
soup = BeautifulSoup(respose.text,"html.parser")
test = soup.find(id="auto-channel-lazyload-article")
test1 = test.find(name="h3")
print(test1)