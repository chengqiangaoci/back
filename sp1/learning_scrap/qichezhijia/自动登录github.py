#通过python代码登录github
import requests
from bs4 import BeautifulSoup

#登录页面发送请求
r1 = requests.get("http://github.com/login")
s1 = BeautifulSoup(r1.text,"html.parser")
#获取csrftoken(在input标签，value属性中)
token = s1.find(name="input",attrs={"name":"authenticity_token"}).get("value")#csrftoken
r1_cookie_dict = r1.cookies.get_dict() #有些网站是先提供cookie，等登陆上去后再对这个cookie进行授权
#输入用户名、密码和token一起发送到服务端:以下数据
"""authenticity_token	ulq0JQ3rsEyjYjhOGTeM2oURz6lw8MJxD0+gfhg7pyvS/gfG9So2K8aMmXLbBPWlGZOlRBUty3ozbq+2nBc1hQ==
commit	Sign+in
login	2395618655@qq.com
password	1889100a
utf8	√"""
r2 = requests.post(
	"https://github.com/session",
	data={
	"uft-8":"√",
	"login":"2395618655@qq.com",
	"password":"1889100a",
	"commit":"sign in",
	"authenticity_token":token,
	},
	cookies = r1_cookie_dict
)

r2_cookie_dict = r2.cookies.get_dict()#字典类型的cookies
cookie_dict = {}
cookie_dict.update(r1_cookie_dict)#将两个cookie进行合并
cookie_dict.update(r2_cookie_dict)

#然后就可以用cookie访问任何页面了
r3 = requests.get(
	url="https://github.com/settings/emails",#访问自己账号的email页面
	cookies=cookie_dict
	)#带着cookie
print(r3.text)