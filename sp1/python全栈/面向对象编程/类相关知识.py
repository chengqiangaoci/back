#数据属性：变量
#函数属性：就是方法

#定义类的数据属性
# class Chinese(object):
# 	"""这是一个中国人的类"""
# 	handsome = "chengqian"
# print(Chinese.handsome)

#类的函数属性
# class Chinese():
# 	"""这是一个中国人的类"""
# 	handsome = "chengqian"
# 	def sui():
# 		print("play majiang")
# Chinese.sui()

#查看类的属性
class Chinese():
	"""这是一个中国人的类"""
	handsome = "chengqian"
	def sui():
		print("play majiang")
print(dir(Chinese))#查看类的属性列表，只有属性名
print(Chinese.__dict__)#查看类的属性字典，所有的都有
print(Chinese.__dict__["handsome"])#因为是字典，所以可以索引值
Chinese.__dict__["sui"]()#因为是字典，所以可以打印方法










