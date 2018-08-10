import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
#抽屉网没有token，因此可以直接post
#以下是获取登录文本和cookie
#首先获取没有得到授权的cookie
r0 = requests.get("http://www.chinadny.com/")
r0_cookie_dict = r0.cookies.get_dict()
#发送用户名和cookie
r1 = requests.post(
	"http://www.chinadny.com/Control/Login.ashx",
	data={
	    "Learn":1,
	    "UserName":"ty",
	    "Password":"ty",
	    "sysId":1,
	},
	cookies = r0_cookie_dict
)

r1_cookie_dict = r1.cookies.get_dict()
#然后合并两个cookie
cookie_dict = {}
cookie_dict.update(r0_cookie_dict)
cookie_dict.update(r1_cookie_dict)


respose = requests.get("http://www.chinadny.com/Main.aspx?token=6282114366099456#")
respose.encoding = "gbk"
soup = BeautifulSoup(respose.text,"html.parser")

test = soup.find("A楼")
print(test)
