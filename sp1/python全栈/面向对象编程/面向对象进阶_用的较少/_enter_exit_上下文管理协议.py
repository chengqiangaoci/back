#with open("a.txt") as f
#enter在with时候触发，enter返回的值给予f，exit在with运行结束后触发
# class Open():
# 	def __init__(self,name):
# 		self.name = name
# 	def __enter__(self):#开始
# 		print("执行enter")
# 	def __exit__(self,exc_type,exc_val,exc_tb):#结束
# 		print("执行exit")
# with Open("a.txt") as f:
# 	pass#一下子执行了enter和exit函数



# class Open():
# 	def __init__(self,name):
# 		self.name = name
# 	def __enter__(self):#开始
# 		print("执行enter")
# 	def __exit__(self,exc_type,exc_val,exc_tb):#结束
# 		print("执行exit")
# 		#三个参数分别代表异常的类、值、回溯(Traceback)
# 		print(exc_type)
# 		print(exc_val)
# 		print(exc_tb)
# with Open("a.txt") as f:
# 	print(f)#一下子执行了enter和exit函数
# 	print(fsafafas)#这样会报错,触发异常的时候直接执行exit，然后中断


class Open():
	def __init__(self,name):
		self.name = name
	def __enter__(self):#开始
		print("执行enter")
	def __exit__(self,exc_type,exc_val,exc_tb):#结束
		print("执行exit")
		#三个参数分别代表异常的类、值、回溯(Traceback)
		print(exc_type)
		print(exc_val)
		print(exc_tb)
		#以下的操作使得没有异常，后面的内容会继续执行
		return True#与上面相比增加了一个返回值true
with Open("a.txt") as f:
	print(f)#一下子执行了enter和exit函数
	print(fsafafas)#这样会报错,触发异常的时候直接执行exit，然后中断
	print(f.name)#这个还是不执行，因为exit在运行了，enter不会在运行了
print("xxxxxxxxxxxxxxxxx")#这个会运行