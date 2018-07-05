import time
def consumer(name):
	print("我是[%s]，我准备开始吃包子了" %name)
	while True:
		baozi = yield
		time.sleep(1)
		print("%s 很开心的吧[%s]吃掉了" %(name,baozi))

def producer():
	c1 = consumer("chengqian")
	c2 = consumer("gaoci")
	c1.__next__()
	c2.__next__()
	for i in range(10):
		time.sleep(1)
		c1.send("包子 %s" %i)
		c2.send("包子 %s" %i)
producer()

#next函数与send函数很相似，都能获得生成器的下一个yield后面表达式的值，不同的是send函数可以向生成器传参：
# import time  
# def func(n):  
#     for i in range(0, n):  
#         arg = yield i  
#         print('func:', arg)  
# f = func(10)  
# while True:  
#     print('main:', next(f))  
#     print('main:', f.send(100))  
#     time.sleep(1) 
# 程序首先调用next函数，使得生成器执行到第4行的时候，把i的值0作为next函数的返回值返回，程序输出main:0，然后生成器暂停。
# 程序往下调用send(100)函数，生成器从第四行继续执行，send函数的参数100作为yield的返回值，并赋值给arg，然后得到func:100的输出。
# 简单的说，send函数使得yield关键字拥有了返回值返回给它的左值。