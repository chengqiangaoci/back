from multiprocessing import Process,Pool
import time,os
def Foo(i):
	time.sleep(1)
	print(i)
def Bar(arg):
	print(os.getpid())
	print(os.getppid())
if __name__ == '__main__':
	pool = Pool(5)#进程池中最多一次性运行5个进程
	for i in range(10):#总任务
		#回调函数：就是某个动作或函数执行成功后再去执行的函数
		pool.apply_async(func=Foo,args=(i,),callback=Bar)
	pool.close()#在进程池中close必须放在join前面
	pool.join()
	print("end")


