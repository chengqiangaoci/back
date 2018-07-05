# class Foo():
# 	pass
# f1 = Foo()
# f1()#会报错，因为Foo产生的对象not callable

class Foo():
	def __call__(self,*args,**kwargs):
		print("实例执行")
f1 = Foo()#调用Foo类的__call__
f1()#现在就可以执行了，调用了__call__方法