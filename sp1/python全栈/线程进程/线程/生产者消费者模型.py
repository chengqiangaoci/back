#生产者和消费者通过中间介质来处理，解决强耦合问题
#通过队列
import time,random
import queue,threading

q = queue.Queue()
def Producer(name):
	count = 0
	while count < 10:
		print("making........")
		time.sleep(random.randrange(3))#产生一个随机数，1或者2之间
		q.put(count)
		print("Producer %s has produced %s baozi.." %(name,count))
		count += 1
		q.task_done()#put一个后发送信号给它
		print("ok........")
def Consumer(name):
	count = 0
	while count < 10:
		time.sleep(random.randrange(4))
		if not q.empty():
			data = q.get()
			q.join()#有包子才会显示
			print("consumer %s has eat %s baozi..." %(name,data))
		else:
			print("--no baozi anymore--")
		count += 1
p1 = threading.Thread(target=Producer,args=("A",))
p2 = threading.Thread(target=Consumer,args=("B",))
p3 = threading.Thread(target=Consumer,args=("C",))
p4 = threading.Thread(target=Consumer,args=("D",))

p1.start()
p2.start()
p3.start()
p4.start()















