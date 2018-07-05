class ChinesePeople():
	country = "China"
	def __init__(self,name):
		self.name = name
	def play_ball(self,ball):
		print("%s 正在打 %s" %(self.name,ball))
	def say_word(self,word):
		print("%s 说 %s" %(self.name,word))

#查看类属性
# print(ChinesePeople.country)

#修改类属性
# ChinesePeople.country = "CHINA"
# print(ChinesePeople.country)

#删除类属性
# del ChinesePeople.country
# print(ChinesePeople.country)

#增加类属性
# ChinesePeople.location = "Asia"
# print(ChinesePeople.location)











