#异常分为语法错误和逻辑错误

#异常处理:1、if判断式
# while True:
# 	age = input(">>:请输入")
# 	if age.isdigit():
# 		print(int(age))
# 	elif age.isspace():
# 		print("您输入的是空格，请重试")
# 	elif len(age) == 0:
# 		print("您没有输入，请重试")
# 	else:
# 		print("其它的非法输入")
# 		break


#异常处理:2、python为每一种异常定制了一个类型，然后提供一种特定的语法结构来进行异常处理
# try:
# 	age = input(">>:请输入")
# 	int(age)#主逻辑

# 	num2 = input(">>:请输入")
# 	int(num2)
# except ValueError as e:
# 	print(e)



#万能异常Exception
try:
	age = input(">>:请输入")
	int(age)#主逻辑

	num2 = input(">>:请输入")
	int(num2)

	l = []
	l[10000]

	dic= {}
	dic["name"]
except Exception as e:#万能异常
	print(e)
