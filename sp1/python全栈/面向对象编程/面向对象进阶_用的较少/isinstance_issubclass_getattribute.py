# class Foo():
# 	pass
# class Bar(Foo):
# 	pass
# f1 = Foo()
# print(isinstance(f1,Foo))#f1是否是Foo的实例
# print(issubclass(Bar,Foo))#Bar是否是Foo的子类


#先看__getattr__
# class Foo():
# 	def __init__(self,x):
# 		self.x = x

# 	def __getattr__(self,item):
# 		print("执行的是我")
# 		#return self.__dict__[item]
# f1 = Foo(10)
# print(f1.x)
# f1.name


#再看getattribute
class Foo():
	def __init__(self,x):
		self.x = x

	def __getattr__(self,item):
		print("执行的是getattr")
		#return self.__dict__[item]

	def __getattribute__(self,item):
		print("执行的是getattribute")
		raise AttributeError("抛出异常了")#给getattr下达指令
f1 = Foo(10)
f1.x#虽然这里x存在，但是也执行attribute
f1.name#这里就是执行的getattribute