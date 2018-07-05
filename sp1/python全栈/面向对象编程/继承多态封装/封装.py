#封装可以理解为将数据属性和函数属性私有化


#约定一：以单下划线开头的名字都是内部的，私有的
#这样的话from module import *不能被导入
#但是from module import _private_module依然可以导入
class People():
	_star = "earth"
	#__star = "earth" 双下划线的话，下面就不能打印
	def __init__(self,id,name,age,salary):
		self.id = id
		self.name = name
		self.age = age
		self.salary = salary

	def get_id(self):
		print("我是私有方法阿，我找到的id是[%s]" %self.id)
p1 = People("12323","alex","18",100000)
print(p1._star)#这里可以正常打印


#约定二：双下划线开头的名字外部无法被访问


