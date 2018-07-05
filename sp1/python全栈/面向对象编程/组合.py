# class Hand():
# 	pass
# class Foot():
# 	pass
# class Trunk():
# 	pass
# class Head():
# 	pass
# class Person():
# 	def __init__(self,id_num,name):
# 		self.id_num = id_num
# 		self.name = name#这些属性也可以单独为类
# 		self.hand = Hand()
# 		self.foot = Foot()
# 		self.trunk = Trunk()
# 		self.head = Head()
# p1 = Person("111","alex")
# print(p1.__dict__)


#组合
class School():
	def __init__(self,name,addr):
		self.name = name
		self.addr = addr
	def recruit(self):
		print("%s 正在招生" %self.name)
class Course():
	def __init__(self,name,price,period,school):
		self.name = name
		self.price = price
		self.period = period
		self.school = school
s1 = School("oldboy","北京")
s2 = School("oldboy","南京")
s3 = School("oldboy","东京")
c1 = Course("linux",10,"1h",s1)#这里传入的是s1
# print(c1.__dict__)
#c1.school#实际上就是s1
# print(c1.school.name)#相当于print(s1.name)

#做一个选课系统，用户可以做选择
# message ="""
# 1 老男孩北京
# 2 老男孩南京
# 3 老男孩东京
# """
while True:
	#print(message)
	menu = {
		"1":s1,
		"2":s2,
		"3":s3
	}
	choice = input("选择学校>>:")
	school_obj = menu[choice]

	name = input("课程名>>:")
	price = input("课程费用>>:")
	period = input("课程周期>>:")

	new_course = Course(name,price,period,school_obj)
	print('课程【%s】属于【%s】学校' %(new_course.name,new_course.school_obj))