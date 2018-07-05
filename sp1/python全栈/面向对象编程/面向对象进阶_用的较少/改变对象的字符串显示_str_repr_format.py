# class Foo():
# 	def __init__(self,name,age):
# 		self.name = name
# 		self.age = age

# 	def __str__(self):
# 		return "名字是%s 年龄是%s" %(self.name,self.age)
# #repr是str的替代品，找不到str就会找repr
# 	def __repr__(self):
# 		return "名字是%s 年龄是%s" %(self.name,self.age)
# f1 = Foo("egon",18)
# print(f1.__str__())
# print(f1)#跟上面的效果一样


# x = "{0}{1}{0}".format("dog","cat")
# print(x)
class Date():
	def __init__(self,year,mon,day):
		self.year = year
		self.mon = mon
		self.day = day
	def __format__(self,format_spec):
		print("i am done")
		return "{0.year}{0.mon}{0.day}".format(self)
d1 = Date(2018,2,28)
print(format(d1))