#装饰器本质上就是函数，为其它函数添加附加功能
#原则：不修改被修饰函数的源代码、调用方式
#装饰器=高阶函数+函数嵌套+闭包
#创建一个装饰器，使得以下函数cal具有统计运行时间的功能
# import time
# def timmer(func):
# 	def wrapper(*args,**kwargs):
# 		start_time = time.time()
# 		res = func(*args,**kwargs)
# 		stop_time = time.time()
# 		print("函数运行时间是%s" %(stop_time-start_time))
# 		return res
# 	return wrapper
# @timmer
# def cal(l):
# 	res = 0
# 	for i in l:
# 		res += i
# 	return res
# res = cal(range(20))
# print(res)

#高阶函数：函数接受的参数是一个函数名或函数的返回值是一个函数名
# def foo():
# 	print("你好")
# def test(func):#这就是一个高阶函数
# 	print(func)#打印内存地址
# 	func()#打印你好
# test(foo)

#函数嵌套：在函数里下一层也有函数
# def father(name):
# 	def son():
# 		print("my father is %s" %name)
# 		def grandson():
# 			print("xxxx is %s" %name)
# 		grandson()#再执行里层
# 	son()#嵌套的函数需要有调用,先执行最外层
# father("chengqian")
#以上就是闭包，封装了变量（包括函数）
#闭包融合在函数嵌套里

#装饰器实现
#装饰器框架
import time
def timmer(func):#func=test
	def wrapper(*args,**kwargs):
		#print(func)#获取内存地址
		start_time = time.time()
		res1 = func(*args,**kwargs)#运行了test函数
		stop_time = time.time()
		print("运行时间是%s" %(stop_time-start_time))
		return res1
	return wrapper#这里需要形成闭包
@timmer
def test():
	time.sleep(1)
	print("test函数运行完毕")
	return "这是test的返回值"
# res = timmer(test)#返回的是wrapper的地址
# res()#执行的是wrapper()

res = test()
print(res)
#@timmer相当于test=timmer(test)，也就是语法糖
#然后就可以直接运行test()















































