#类属性，数据描述符，实例属性，非数据描述符，找不到的属性触发__getattr__()
# class Foo():
# 	def __get__(self,instance,owner):
# 		print("get方法")
# 	def __set__(self,instance,value):
# 		print("set方法")
# 	def __delete__(self,instance):
# 		print("delete方法")
# class Bar():
# 	x = Foo()#描述符
# Bar.x=1#类属性,触发get函数
# print(Bar.x)


class Foo():
	def __get__(self,instance,owner):
		print("get方法")
	def __set__(self,instance,value):
		print("set方法")
	def __delete__(self,instance):
		print("delete方法")
class Bar():
	x = Foo()#描述符
b1 = Bar()
b1.x = 1#触发set方法







