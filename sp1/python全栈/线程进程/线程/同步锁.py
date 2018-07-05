#需求：num减100次1直至到0，开100个线程
# num=100
# def sub():
# 	global num
# 	num -= 1
# 	return num
# import threading
# l = []
# for i in range(100):#100个线程
# 	t = threading.Thread(target=sub)
# 	t.start()
# 	l.append(t)
# for i in l:
# 	t.join()#等着主线程，等子线程结束后再一起结束
# print(num)


#以下结果不是0，原因是：
#第一个线程返回num的速度大于CPU轮询的速度，结果第二个线程拿不到num的返回值
# import threading
# import time
# num=100
# def sub():
# 	global num
# 	temp = num
# 	time.sleep(0.001)#间接导致阻塞IO，在等待的时候，第二个线程却来了，结果第二个线程拿到的值也是temp=num=100
# 	num = temp-1
# 	return num
# l = []
# for i in range(100):#100个线程
# 	t = threading.Thread(target=sub)
# 	t.start()
# 	l.append(t)
# for i in l:
# 	t.join()#等着主线程，等子线程结束后再一起结束
# print(num)


#解决办法：同步锁，不让sub下面的函数在CPU中不切换
import threading
import time
num=100
lock = []
lock = threading.Lock()
def sub():
	lock.acquire()#获取锁
	global num
	temp = num
	time.sleep(0.001)#有了进程锁后，0.001秒后才会有下一个线程进来
	num = temp-1
	lock.release()#释放锁
l = []
for i in range(100):#100个线程
	t = threading.Thread(target=sub)
	t.start()
	l.append(t)
for i in l:
	t.join()#等着主线程，等子线程结束后再一起结束
print(num)


