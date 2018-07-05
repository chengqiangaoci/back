#需求：多线程将列表中最后一个元素不断的取出
#以下是单线程举例
# import threading,time
# li = [1,2,3,4,5]
# def pri():
# 	while li:#判断li是否是空的
# 		a = li[-1]
# 		print(a)
# 		time.sleep(1)
# 		try:
# 			li.pop()#或者remove(a)
# 		except Exception as e:
# 			print("---",a,e)
# pri()



#以下由于同步的问题会报错
# import threading,time
# li = [1,2,3,4,5]
# def pri():
# 	while li:#判断li是否是空的
# 		a = li[-1]
# 		print(a)
# 		time.sleep(1)
# 		li.remove(a)
# t1 = threading.Thread(target=pri)
# t1.start()
# t2 = threading.Thread(target=pri)
# t2.start()



#队列在多线程中保障线程的安全
# import queue#线程队列
# q = queue.Queue()#参数用来限制放入的数据个数
# #默认队列数据先进先出模式
# q.put(12)#放入数据
# q.put("hello")
# q.put({"name":"chengqian"})
# while 1:
# 	data = q.get()
# 	print(data)#一个个取
# 	print("-----------")



#先进后出模式
# import queue
# q = queue.LifoQueue()
# q.put(12)
# q.put("hello")
# q.put({"name":"chengqian"})
# while 1:
# 	data = q.get()
# 	print(data)#一个个取
# 	print("-----------")



#优先级模式
import queue
q = queue.PriorityQueue()
q.put([3,12])
q.put([2,"hello"])#最早出来
q.put([4,{"name":"chengqian"}])
while 1:
	data = q.get()
	print(data)#一个个取
	print("-----------")