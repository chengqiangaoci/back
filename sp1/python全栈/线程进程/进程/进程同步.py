#进程也会出现同步的情况，如共用屏幕，每个进程都想在上面打印东西
# from multiprocessing import Process,Lock
# def f(i):
# 	print("hello world %s" %i)
# if __name__ == '__main__':
# 	for num in range(10):
# 		Process(target=f,args=(num,)).start()#在cmd上会出现抢屏幕的情况


from multiprocessing import Process,Lock
def f(l,i):
	l.acquire()
	print("hello world %s" %i)
	l.release()
if __name__ == '__main__':
	lock = Lock()
	for num in range(10):
		Process(target=f,args=(lock,num)).start()

