def test(x):
	"""x+1"""
	x += 1
	return x

test(3)#这里只是test(3)，但是没有函数或变量来接受结果，因此none
print(test(3))#print()接受结果

#函数的优势：代码重用、保持一致性、易维护、可扩展

# 函数的参数
# 形参只在函数内部有效，调用结束返回主调用函数后则不能再使用该函数
# Return函数碰到一个就结束了
# def test(x,y):
# 	ruturn x
# 	ruturn y

# print(test(2,3))#这就就只打印x了，因为第一个return后就返回

# #一般都会在形参数里放入一个*args以备意外（可扩展性），元组
# def test(x,*args):
# 	print(x)
# 	print(args)

# test(1,2,3,4,5,6)#这里执行就会发现2,3,4,5,6在元祖里

# #**kargs对于关键字参数（xx=xx的实参形式）
# def test(x,**kwargs):
# 	Print(x)
# 	Print(kwargs)

# test(1,y=2,z=3)#这里就是出现的字典（实参中出现xx=xx）

#一定要注意args一定要在kwargs前面！！！！！


























