#__两个下划线开头，声明该方法为私有方法，不能在类地外部调用,即不能被实例调用
# class Vehicle():#定义交通工具
# 	Country = "China"
# 	def __init__(self,name,speed,load,power):
# 		self.name = name
# 		self.speed = speed
# 		self.load = load
# 		self.power = power
# 	def run(self):
# 		print("开动了")
# class Subway(Vehicle):#地铁
# 	def __init__(self,name,speed,load,power,line):
# 		# self.name = name
# 		# self.speed = speed
# 		# self.load = load
# 		# self.power = power
# 		Vehicle.__init__(self,name,speed,load,power)#调用父类的数据属性，但是要参数
# 		self.line = line#这是子类自己新增加的
# 	def show_info(self):
# 		Vehicle.run(self)#调用父类的函数属性
# 		print(self.name,self.line)
# line13 = Subway("武汉地铁","10KM/S",10000,"电",2)
# line13.show_info()


#super调用父类的关系
class Vehicle():#定义交通工具
	Country = "China"
	def __init__(self,name,speed,load,power):
		self.name = name
		self.speed = speed
		self.load = load
		self.power = power
	def run(self):
		print("开动了")
class Subway(Vehicle):#地铁
	def __init__(self,name,speed,load,power,line):
		# self.name = name
		# self.speed = speed
		# self.load = load
		# self.power = power
		super().__init__(name,speed,load,power)#super不需要self
		self.line = line#这是子类自己新增加的
	def show_info(self):
		super().run()#调用父类的函数属性
		print(self.name,self.line)
line13 = Subway("武汉地铁","10KM/S",10000,"电",2)
line13.show_info()
