import requests
from bs4 import BeautifulSoup
#抽屉网没有token，因此可以直接post
#以下是获取登录文本和cookie
#首先获取没有得到授权的cookie
r0 = requests.get("http://dig.chouti.com/")
r0_cookie_dict = r0.cookies.get_dict()
#发送用户名和cookie
r1 = requests.post(
	"http://dig.chouti.com/login",
	data={
	    "phone":"8615607170206",
	    "password":"1889100b",
	    "oneMonth":1,
	},
	cookies = r0_cookie_dict
)

r1_cookie_dict = r1.cookies.get_dict()
#然后合并两个cookie
cookie_dict = {}
cookie_dict.update(r0_cookie_dict)
cookie_dict.update(r1_cookie_dict)
#然后是点赞行为，在这里是一个post行为
r2 = requests.post("http://dig.chouti.com/link/vote?linksId=17283306",
	cookies=cookie_dict)
print(r2.text)#点赞成功后的相应提示 