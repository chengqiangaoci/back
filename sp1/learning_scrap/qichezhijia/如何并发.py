#同时爬取几个网站
url_list = ["http://www.cnblogs.com/wupeiqi/articles/6229292.html",
"http://www.baidu.com",
"http://www.xiaohua.com",
]
#首先是串行方法,但是耗时比较长
# import requests
# for url in url_list:
# 	respose = requests.get(url)
# 	print(respose.content)
# 	print("=======================")

#然后是线程或进程
import requests
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor#导入线程和进程池
def task(url):
	respose = requests.get(url)
	print(respose.content)

pool = ThreadPoolExecutor(10)#10个任务一次并发
for url in url_list:
	pool.submit(task,url)#函数和参数

pool.shutdown(wait=True)#完成任务后进行等待


#然后是异步非阻塞
#比如烧水，同步阻塞就是一直等着水烧开；同步非阻塞就是去看电视，但是要时不时回来看水开了没；
#          异步阻塞就是设置警报提醒水开了，但是人还在这等着；
#          异步非阻塞就是设置警报水开了，人就可以安心看电视去。
#就是说，异步相对于同步来说可以设置通知，非阻塞相对于阻塞来说可以去干其他事。
