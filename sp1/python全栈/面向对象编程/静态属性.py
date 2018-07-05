# class Room():
# 	def __init__(self,name,owner,width,length,heigh):
# 		self.name = name
# 		self.owner = owner
# 		self.width = width
# 		self.length = length
# 		self.heigh = heigh
# 	@property#结合下面的调用，这个装饰器的作用是让你忽视函数数据的逻辑
# 	def cal_area(self):
# 		print("%s 住的 %s 总面积是%s" %(self.owner,self.name,self.width*self.length))
# r1 = Room("厕所","alex",100,100,10000)
# r1.cal_area()
# r1.cal_area#多了这个装饰器后，这样就可以运行了


#调用类方法
class Room():
	tag = 1
	def __init__(self,name,owner,width,length,heigh):
		self.name = name
		self.owner = owner
		self.width = width
		self.length = length
		self.heigh = heigh
	@property#结合下面的调用，这个装饰器的作用是让你忽视函数数据的逻辑
	def cal_area(self):
		print("%s 住的 %s 总面积是%s" %(self.owner,self.name,self.width*self.length))
	def test(self):
		print("from test",self.name)
#首先是类当中的数据属性
print(Room.tag)
#然后是类当中的函数属性
Room.test()