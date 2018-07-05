#由于GIL的存在，python中的多线程并不是真正的多线程，因此python大多数情况下使用多进程

#调用方式1
# from multiprocessing import Process#解决GIL问题
# import time
# def f(name):
# 	time.sleep(1)
# 	print("hello",name,time.ctime())

# if __name__ == '__main__':
# 	p_list = []
# 	for i in range(50):
# 		p = Process(target=f,args=("alvin",))
# 		p_list.append(p)
# 		p.start()
# 	for i in p_list:
# 		i.join()
# 	print("end")




#调用方式2
# from multiprocessing import Process
# import time
# class MyProcess(Process):
# 	def __init__(self):
# 		super(MyProcess,self).__init__()
# 		#self.name = name
# 	def run(self):
# 		time.sleep(1)
# 		print("hello",self.name,time.ctime())

# if __name__ == '__main__':
# 	p_list = []
# 	for i in range(3):
# 		p = MyProcess()
# 		#p.daemon = True#守护进程,跟线程有所区别
# 		p_list.append(p)
# 		p.start()
# 	for i in p_list:
# 		i.join()
# 	print("end")




#获取进程ID
from multiprocessing import Process
import time
import os
def info(title):
	print("title:",title)
	print("parent process:",os.getppid())#父进程
	print("process id:",os.getpid())#本身进程
def f(name):
	info("function f")
	print("hello",name)
if __name__ == '__main__':
	info("main process line")
	time.sleep(1)
	print("-------------")
	p = Process(target=info,args=("chengqian",))
	p.start()



# import time
# from multiprocessing import Process
# class MyProcess(Process):
# 	def __init__(self,num):
# 		super(MyProcess,self).__init__()
# 		self.num = num
# 	def run(self):
# 		time.sleep(1)
# 		print(self.pid)
# 		print(self.is_alive())
# 		print(self.num)
# 		time.sleep(1)

# if __name__ == '__main__':
# 	p_list = []
# 	for i in range(10):
# 		p = MyProcess(i)
# 		p_list.append(p)

# 	for p in p_list:
# 		p.start()
# 	print("main process end")



