#__getattr__
#如果有属性的话，不调用attr，如果不存在这个属性，就会调用attr函数
class Foo():
	def __init__(self,name):
		self.name = name

	def __getattr__(self,item):
		print("你找的属性【%s】不存在" %item)
f1 = Foo("chengqian")
print(f1.name)
# #找不到age，然后age传给getattr函数的item
# print(f1.age)#正常情况下这个会报错，但是这里会调用getattr函数


#__setattr__
# class Foo():
# 	def __init__(self,name):
# 		self.name = name

# 	def __getattr__(self,item):
# 		print("你找的属性【%s】不存在" %item)

# 	def __setattr__(self,k,v):#操作属性字典
# 		print("执行setattr",k,v)
# 		#要将设置的属性加入字典f1.__dict__
# 		self.__dict__[k] = v
# f1 = Foo("chengqian")#这里直接会打印“执行setattr name chengqian”
# f1.age = 18#这里会打印“执行setattr age 18”
# f1.gender = "male"
# print(f1.__dict__)


#__delattr__
# class Foo():
# 	def __init__(self,name):
# 		self.name = name

# 	def __getattr__(self,item):
# 		print("你找的属性【%s】不存在" %item)

# 	def __setattr__(self,k,v):
# 		print("执行setattr",k,v)
# 		self.__dict__[k] = v
# 	def __delattr__(self,item):
# 		print("执行delattr",item)
# 		#执行真正的删除操作,没有这一行的话就是不许删除属性
# 		self.__dict__.pop(item)
# f1 = Foo("chengqian")
# del f1.name#触发了__delattr__函数
# print(f1.__dict__)#这里打印的就是空字典























