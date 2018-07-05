#在线程间共享多个资源时，如果两个线程分别占有一部分资源并且同时等待对方的资源
#就会造成死锁，因为系统判断这部分资源都正在使用。
# import threading
# import time
# class MyThread(threading.Thread):
# 	def actionA(self):
# 		A.acquire()
# 		print(self.name,"gotA",time.ctime())#这里的self.name是线程名字
# 		time.sleep(2)
# 		B.acquire()
# 		print(self.name,"gotB",time.ctime())
# 		time.sleep(1)
# 		B.release()
# 		A.release()
# 	def actionB(self):
# 		B.acquire()
# 		print(self.name,"gotB",time.ctime())
# 		time.sleep(2)
# 		A.acquire()
# 		print(self.name,"gotA",time.ctime())
# 		time.sleep(1)
# 		A.release()
# 		B.release()
# 	def run(self):
# 		self.actionA()
# 		self.actionB()
# if __name__ == '__main__':
# 	A = threading.Lock()
# 	B = threading.Lock()
# 	L = []
# 	for i in range(5):
# 		t = MyThread()#因为参数里已经继承了类，所以这里就是创建了一个线程
# 		t.start()
# 		L.append(t)
# 	for i in L:
# 		i.join()
# 	print("ending")



#解决：第二个线程拿锁时，让第一个线程不拿锁，这就是递归锁
#递归锁比同步锁中就多了个计数器，大于0时其它线程不能拿到锁
import threading
import time
class MyThread(threading.Thread):
	def actionA(self):
		r_lock.acquire()
		print(self.name,"gotA",time.ctime())#这里的self.name是线程名字
		time.sleep(2)
		r_lock.acquire()
		print(self.name,"gotB",time.ctime())
		time.sleep(1)
		r_lock.release()
		r_lock.release()
	def actionB(self):
		r_lock.acquire()
		print(self.name,"gotB",time.ctime())
		time.sleep(2)
		r_lock.acquire()
		print(self.name,"gotA",time.ctime())
		time.sleep(1)
		r_lock.release()
		r_lock.release()
	def run(self):#这个是thread.run函数！！！！！运行的意思，跟t.start()一样
		self.actionA()
		self.actionB()
if __name__ == '__main__':
	r_lock=threading.RLock()
	L = []
	for i in range(5):
		t = MyThread()#因为参数里已经继承了类，所以这里就是创建了一个线程
		t.start()
		L.append(t)
	for i in L:
		i.join()
	print("ending")







