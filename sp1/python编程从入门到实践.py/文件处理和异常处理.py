# 已存在文件test.txt
with open("test.txt","r") as f:
	#print(f.read())
	print(f.readlines())#列表打印出来

#w 模式是覆盖原有的内容，如果想附加，可以使用 a


#使用try-except代码块时，即便出现异常，程序也可以继续运行
# try:
# 	print(5/0)
# except ZeroDivisionError:
# 	print("you can't divide by zero")
# print("this is a test")
















