import threading#线程
#以下是一个单线程
# import time
# def Hi(number):
# 	print("hello %s" %number)
# 	time.sleep(3)
# if __name__ == "__main__":
# 	Hi(11)



# import time
# def Hi(number):
# 	print("hello %s" %number)
# 	time.sleep(3)
# if __name__ == "__main__":
# 	#t1是对象
# 	t1 = threading.Thread(target=Hi,args=(10,))#Thread是一个类，这个地方的操作是实例化
# 	t1.start()

# 	t2 = threading.Thread(target=Hi,args=(9,))
# 	t2.start()
# 	print("ending.............")


# import time
# def music():
# 	print("begin to listen %s"%time.ctime())
# 	time.sleep(3)
# 	print("stop to listen %s"%time.ctime())

# def game():
# 	print("begin to game %s" %time.ctime())
# 	time.sleep(5)
# 	print("stop to game %s" %time.ctime())
# if __name__ == "__main__":
# 	t1 = threading.Thread(target=music)
# 	t1.start()
# 	t2 = threading.Thread(target=game)
# 	t2.start()
# 	print("ending")#这个ending会跟begin一起打印，然后再打印stop



#join方法
import time
def music():
	print("begin to listen %s"%time.ctime())
	time.sleep(3)
	print("stop to listen %s"%time.ctime())

def game():
	print("begin to game %s" %time.ctime())
	time.sleep(5)
	print("stop to game %s" %time.ctime())
if __name__ == "__main__":
	t1 = threading.Thread(target=music)
	t1.start()
	t2 = threading.Thread(target=game)
	t2.start()
	#t1.join()#t1执行完后才执行主线程
	t2.join()
	print("ending")#这个ending会在最后打印



# import time
# def music():
# 	print("begin to listen %s"%time.ctime())
# 	time.sleep(3)
# 	print("stop to listen %s"%time.ctime())

# def game():
# 	print("begin to game %s" %time.ctime())
# 	time.sleep(5)
# 	print("stop to game %s" %time.ctime())
# if __name__ == "__main__":
# 	t1 = threading.Thread(target=music)
# 	t1.start()
# 	t2 = threading.Thread(target=game)
# 	t2.start()
# 	t1.join()#t1执行完后才执行主线程
# 	print("ending")#这个ending会在最后打印






