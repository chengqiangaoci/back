class Chinese():
	"""这是一个中国人的类"""
	handsome = "chengqian"
	def __init__(self,name,age,gender):#自动return，下面不用加
		self.name = name#这个结合面向对象设计理解
		self.age = age
		self.gender = gender#通过self封装到字典
		#这里就不用return了
	def sui():
		print("play majiang")
	def chadui(self,time):
		print("%s %s 插队了" %(self.name,time))#这里一定要有self
	def eat(self,food):
		print("%s 正在吃%s" %(self.name,food))
p1 = Chinese("chengqian",18,"man")#产生一个实例对象
print(p1.handsome)#风湿理论，在字典上一层找
print(p1.__dict__)#获取字典内容
#Chinese.chadui(p1)
p1.chadui("12")#这里面实际上给了一个p1的参数，不报错
#p1.sui()#这里也给了一个p1的参数，但是没有位置，报错，python自动把p1传入
p1.eat("肉肉")

