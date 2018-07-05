#1、列举布尔值为false的值
# o False "" [] () {} None

#2、根据范围获取其中3和7整除的所有数的和，并返回调用者
#符合条件的数字个数以及数字的总和
# def func(start,end,a=0,b=0):
# 	# a = 0#数量
# 	# b = 0#和
# 	if start == end:
# 		return a,b
# 	if start%3 == 0 and start%7 == 0:
# 		a += 1
# 		b += start
# 	ret = func(start+1,end,a,b)
# 	return ret
# ret = func(1,7)
# print(ret)

#3、三元函数
# python的三元运算书写格式：
# 变量名 = 变量1 if 条件判断成立 else 变量2
# 解释：条件成立 变量名值为变量1 否则为变量2

# 4、test = lambda x : x + 1#匿名函数
# print(test(10))

#5、使用set集合获取[11,22,33]和[22,33,44]中相同的元素集合
# test1 = [11,22,33]
# test2 = [22,33,44]
# python1 = set(test1)
# python2 = set(test2)
# python = python1&python2
# print(python)

#6、定义函数统计字符串中大小写字母以及数字的个数，并以字典为结果返回给调用者
# def num(name):
# 	a = 0
# 	b = 0
# 	c = 0
# 	for i in name:
# 		if i.isupper():
# 			a += 1
# 		elif i.islower():
# 			b += 1
# 		elif i.isdigit():
# 			c += 1
# 	return a,b,c

#7、简述函数的位置参数、关键字参数、默认参数、可变长参数的特点以及注意事项
# 位置参数：按形参的位置传入，叫位置参数就是普通参数

# 关键字参数：传入实参时指定形参的值

# 默认参数：形参直接指定默认值的参数

# 可变长参数：*args **kwargs，一个只能接收没有位置参数的实参或参入的列表，元组，俩可以接收关键字参数和字典格式。

#8、简述 Python3 中的 range 函数和 Python2.7 中的 range 函数有什么区别?
# 区别：在于返回值的不同
# python3.x range 不会生成值，只有用的时候才会生成
# python2.x range 会直接生成一个列表，值已经生成

#9、内置函数 all 和 any 的区别
# all   : 当传入空可迭代对象时返回True，当可迭代对象中有任意一个不为True，则返回False
# any : 当传入空可迭代对象时返回False，当可迭代对象中有任意一个不为False，则返回True

#10将字符串程前转换为utf-8编码的字节类型
# name = "程前"
# print(name)
# print(bytes(name,encoding="utf-8"))#将字符串转换为字节对象
# print(bytes(name, encoding='utf-8').decode('utf-8'))

#11、encode和decode的区别
# 字符串在Python内部的表示是unicode编码，因此，在做编码转换时，通常需要以unicode作为中间编码，
# 即先将其他编码的字符串解码（decode）成unicode，再从unicode编码（encode）成另一种编码。
# s='中文'
# s=s.decode('utf-8')   #将utf-8编码的解码成unicode
# print isinstance(s,unicode)   #此时输出的就是True
# s=s.encode('utf-8')           #又将unicode码编码成utf-8
# print isinstance(s,unicode)   #此时输出的就是False

#zip函数,获取一个带列表，列表里是元组
# l1 = ["alex", 22, 33, 44, 55]
# l2 = ["is", 22, 33, 44, 55]
# l3 = ["good", 22, 33, 44, 55]
# l4 = ["guy", 22, 33, 44, 55]
# n1 = list(zip(l1,l2,l3,l4))
# n2 = n1[0]
# n3 = '_'.join(n2)
# print(n3)







































































