#之前大多使用get去请求数据，这里使用post将数据推送给网络服务器进行存储和分析
#提交一个基本表单
#源网址http://pythonscraping.com/pages/files/form.html
# import requests
# name = {"firstname":"Ryan","lastname":"Mitchell"}
# r = requests.post("http://pythonscraping.com/pages/files/processing.php",data=name)#这里的网址是在post时出现的网址
# print(r.text)


#提交文件和图像
#源网址http://pythonscraping/files/form2.html
# import requests
# files = {"uploadFile":open("../files/Python-logo.png","rb")}#这里用open函数打开的Python文件对象
# r = requests.post("http://www.pythonscraping.com/files/processing2.php",files=files)
# print(r.text)


#处理登录和cookies(即保存登录状态)
#源网址http://pythonscraping.com/pages/cookies/login.html
# import requests
# p = {"username":"chengqian","password":"password"}
# r = requests.post("http://www.pythonscraping.com/pages/cookies/welcome.php",{"username":"chengqian","password":"password"})
# print("Cookie is set to:")
# print(r.cookies.get_dict())#获取cookies并赋予r.cookies
# print("----------------")
# print("Going to profile page..")
# r = requests.get("http://www.pythonscraping.com/pages/cookies/profile.php",cookies=r.cookies)#这里的网址是未登录的
# print(r.text)


#如果网站比较复杂，经常调整cookie或者你葱一开始就不想用cookie，可以使用session函数
# import requests
# session = requests.Session()
# params = {"username":"username","password":"password"}
# s = session.post("http://www.pythonscraping.com/pages/cookies/welcome.php",params)
# print("Cookie is set to:")
# print(s.cookies.get_dict())
# print("----------------")
# print("Going to profile page..")
# s = session.get("http://www.pythonscraping.com/pages/cookies/profile.php")
# print(s.text)


#Http基本接入认证
#源网址http://www.pythonscraping.com/pages/auth/login.php
import requests
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth
auth = HTTPBasicAuth("chengqian","password")
r = requests.post(url="http://www.pythonscraping.com/pages/auth/login.php",auth=auth)
print(r.text)




