#并发：是指系统具有处理多个任务(动作)的能力
#并行：是指系统具有同时处理多个任务(动作)的能力

#同步：当进程执行到一个IO(等待外部数据)的时候，等就是同步
#异步：当进程执行到一个IO(等待外部数据)的时候，不等，一直等到数据接收成功再回来处理

#并行
# def add():
# 	sum = 0
# 	for i in range(100000):
# 		sum += i
# 	print(sum)

# def mul():
# 	sum2 =1
# 	for i in range(1,100000):
# 		sum2 *= i
# 	print(sum2)
# import threading,time
# start = time.time()
# t1 = threading.Thread(target=add)
# t2 = threading.Thread(target=mul)
# l = []
# l.append(t1)
# l.append(t2)

# for t in l:
# 	t.start()
# for t in l:
# 	t.join()
# print("cost time %s" %(time.time()-start))#这个花了11.5秒


#串行
def add():
	sum = 0
	for i in range(100000):
		sum += i
	print(sum)

def mul():
	sum2 =1
	for i in range(1,100000):
		sum2 *= i
	print(sum2)
import threading,time
start = time.time()
add()
mul()
print("cost time %s" %(time.time()-start))#这个花了11.4秒
#反而并行比串行花的时间更多
#因为多核没利用上


#以上的问题就是因为GIL
#GIL：全局解释锁
#无论开启多少线程，多少个CPU，python在同一时刻只允许一个线程运行















