# class Room():
# 	def __init__(self,name,width,length):
# 		self.name = name
# 		self.width = width
# 		self.length = length
# 	@property#将方法伪装成属性area=property(area)
# 	def area(self):
# 		return self.width*self.length
# r1 = Room("测试",1,1)
# print(r1.area)

class Lazeproperty():
	def __init__(self,func):
		self.func = func
	def __get__(self,instance,owner):
		val = self.func(instance)
		return val
class Room():
	def __init__(self,name,width,length):
		self.name = name
		self.width = width
		self.length = length
	@Lazeproperty
	def area(self):
		return self.width*self.length
r1 = Room("测试",1,1)
print(r1.area)









