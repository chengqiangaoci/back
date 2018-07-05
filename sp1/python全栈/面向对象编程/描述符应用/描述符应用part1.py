#描述符就是一个新式类，至少实现了get，set，delete中的一个，这也被称为描述符协议
class People():
	def __init__(self,name,age,salary):
		self.name = name
		self.age = age
		self.salary = salary
p1 = People("chengqian",27,100000)