#进程之间的数据不共享，使用queue通信
# import queue
# from multiprocessing import Process,Queue
# def foo(q):
# 	q.put(123)
# 	q.put("chengqian")

# if __name__ == '__main__':
# 	q = Queue()#进程队列
# 	p = Process(target=foo,args=(q,))#将主进程中的队列传递给子进程
# 	p.start()
# 	print(q.get())
# 	print(q.get())




#使用管道通信
# from multiprocessing import Process, Pipe

# def f(conn):
# 	conn.send([12, {"name":"yuan"}, 'hello'])
# 	response=conn.recv()
# 	print("response",response)
# 	conn.close()
# 	print("q_ID2:",id(conn))

# if __name__ == '__main__':

# 	parent_conn, child_conn = Pipe()#双向管道
	
# 	print("q_ID1:",id(child_conn))
# 	p = Process(target=f, args=(child_conn,))
# 	p.start()
# 	print(parent_conn.recv())   # prints "[42, None, 'hello']"
# 	parent_conn.send("儿子你好!")
# 	p.join()



#使用manager通信：与上面两个不同的是这个可以共享数据
from multiprocessing import Process, Manager

def f(d, l,n):
	d[n] = '1'
	d['2'] = 2
	d[0.25] = None
	l.append(n)
	#print(l)
	print("son process:",id(d),id(l))

if __name__ == '__main__':
	with Manager() as manager:
		
		d = manager.dict()

		l = manager.list(range(5))

		print("main process:",id(d),id(l))

		p_list = []

		for i in range(10):
			p = Process(target=f, args=(d,l,i))
			p.start()
			p_list.append(p)

		for res in p_list:
			res.join()

		print(d)
		print(l)







