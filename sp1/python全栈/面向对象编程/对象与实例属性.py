# class Chinese():
# 	country = "China"
# 	def __init__(self,name):
# 		self.name = name
# 	def play_ball(self,ball):
# 		print("%s 正在打 %s" %(self.name,ball))
# p1 = Chinese("chengqian")
# print(p1.country)
# p1.country = "Japanese"
# print(Chinese.country)#这里打印类的属性，china
# print(p1.country)#这里打印实例的属性，japanese

#在设定程序的时候，输入输出的内容最好不要写在里面
#以下就不宜
# country = "中国"
# class Chinese():
# 	def __init__(self):
# 		print("——————————>?")
# 		name = input("请输入用户名>>:")
# 		self.name = name
# 	def play_ball(self,ball):
# 		print("%s 正在打 %s" %(self.name,ball))
# p1 = Chinese()
# print(p1.name)

#最好是下面这样
# country = "中国"
# class Chinese():
# 	def __init__(self):
# 		self.name = name
# 	def play_ball(self,ball):
# 		print("%s 正在打 %s" %(self.name,ball))
# def shilihua():
# 	name = input("请输入用户名>>:")
# 	p1 = Chinese()
# 	print(p1.name)
# shilihua()



# country = "中国--------"
# class Chinese():
# 	country = "中国"
# 	def __init__(self,name):
# 		self.name = name
# 	#这里要是.country的话就会在类里面找了 
# 		print(country)#这里可以找到country，这个country和类没有关系
# 	def play_ball(self,ball):
# 		print("%s 正在打 %s" %(self.name,ball))
# p1 = Chinese("chengqian")


country = "中国--------"
class Chinese():
	country = "中国"
	l = ["a","b"]
	def __init__(self,name):
		self.name = name
	#这里要是.country的话就会在类里面找了 
		print(country)#这里可以找到country，这个country和类没有关系
	def play_ball(self,ball):
		print("%s 正在打 %s" %(self.name,ball))
p1 = Chinese("chengqian")
print(p1.l)
# p1.l = [1,23,4]#这是赋值
# print(p1.l)#打印是赋值后的
# print(Chinese.l)#打印是原先的,不会修改
p1.l.append("c")#这是修改
print(p1.l)#打印是修改后的
print(Chinese.l)#打印是修改后的






