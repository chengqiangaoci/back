url_list = ["http://www.cnblogs.com/wupeiqi/articles/6229292.html",
"http://www.baidu.com",
"http://www.xiaohua.com",
]

import requests
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
def bingfa(url):
	respose = requests.get(url)
	print(respose.text)

pool = ThreadPoolExecutor(10)
for url in url_list:
	pool.submit(bingfa,url)
