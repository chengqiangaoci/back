class Chinese():
	country = "China"
	def __init__(self,name):
		self.name = name
	def play_ball(self,ball):
		print("%s 正在打 %s" %(self.name,ball))
	def say_word(self,word):
		print("%s 说 %s" %(self.name,word))
p1 = Chinese("chenqgian")
#查看实例属性字典
# print(p1.__dict__)

#查看实例属性
# print(p1.name)

#增加或修改实例属性
p1.age = 18
print(p1.__dict__)

#删除实例属性
del p1.age
print(p1.__dict__)