#python变量名不能以数字、关键字开头

#条件语句：可以嵌套if

#基本数字类型
#字符串只有加减
#数字有加减乘除
print(39//8) #4 取得是整除
print(39%8)#取的是余数
print(3**2)#取得是平方
print(3**3)#取得是立方

#while循环
#以下是个死循环
# while 1==1:#判断是否满足
# 	print("ok")#满足了就执行这个，然后再回上面再判断一次，循环不断

# #练习题1：使用while循环输入1,2,3,4,5,6,8,9,10
# for i in range(1,11):
# 	if i != 7:
# 		print(i)
# 	else:
# 		continue#也可以pass

# test = 1
# while test < 11:
# 	if test == 7:
# 		pass#这里就不能用continue了
# 	else:
# 		print(test)
# 	test = test + 1

#练习2：求1-100所有的奇数
# for i in range(1,101):
# 	if i%2 != 1:
# 		continue#也可以使用pass
# 	else:
# 		print(i)

# n = 1
# while n < 101:
# 	if n%2 == 0:
# 		pass
# 	else:
# 		print(n)
# 	n = n + 1

#练习3：求1-100所有数的和
# n = 1
# s = 0
# while n < 101:
# 	s = s + n
# 	n = n + 1
# print(s)

# n = 0
# for i in range(1,101):
# 	n = n + i
# print(n)

#练习4：求1-2+3-4+5...99的所有数的和！！！！！！！这个不会
# n = 1
# s = 0
# while n <100:
# 	temp = n % 2
# 	if temp == 0:
# 		s = s - n
# 	else:
# 		s = s + n
# 	n = n + 1
# print(s)

# s = 0
# for i in range(1,100):
# 	if i%2 == 1:
# 		s = s + i
# 	else:
# 		s = s - i
# print(s)#总体来说，这种情况下使用range函数更方便易懂。


#练习5：三次登录机会

n = 1
while n < 4:
	name = input("please enter your name1:")
	password = input("please enter your password1:")
	if name == "chengqian" and password == "188910":
		print("welcome " + name)
		break
	else:
		print("you're wrong,please continue your enter")
	n = n + 1
