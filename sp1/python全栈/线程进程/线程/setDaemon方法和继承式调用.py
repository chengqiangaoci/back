#join：当主线程完成时，如果子线程未完成，那么主线程会等待子线程完成后再退出
#setDaemon：当主线程完成时，不管子线程是否完成，都会跟主线程一起结束
# import threading
# import time
# def LisetnMusic(name):
# 	print("Begin listening to %s. %s" %(name,time.ctime()))
# 	time.sleep(3)
# 	print("ending listening %s" %time.ctime())
# def RecordBlog(title):
# 	print("Begin recording the %s! %s" %(title,time.ctime()))
# 	time.sleep(2)
# 	print("end recording %s" %time.ctime())

# threads = []
# t1 = threading.Thread(target=LisetnMusic,args=("水手",))
# t2 = threading.Thread(target=RecordBlog,args=("python线程",))
# threads.append(t1)
# threads.append(t2)
# if __name__ == '__main__':
# 	for t in threads:
# 		t.start()
# 	t.join()#join的t2，t2的最后一行和11111一起执行
# 	print("1111111111111111")



# import threading
# import time
# def LisetnMusic(name):
# 	print("Begin listening to %s. %s" %(name,time.ctime()))
# 	time.sleep(3)
# 	print("ending listening %s" %time.ctime())
# def RecordBlog(title):
# 	print("Begin recording the %s! %s" %(title,time.ctime()))
# 	time.sleep(3)
# 	print("end recording %s" %time.ctime())

# threads = []
# t1 = threading.Thread(target=LisetnMusic,args=("水手",))
# t2 = threading.Thread(target=RecordBlog,args=("python线程",))
# threads.append(t1)
# threads.append(t2)
# if __name__ == '__main__':
# 	for t in threads:
# 		t.setDaemon(True)#子线程与主线程一起结束。
# 		t.start()
# 		#t.join()#join的t2，t2的最后一行和11111一起执行
# 	print("1111111111111111")






