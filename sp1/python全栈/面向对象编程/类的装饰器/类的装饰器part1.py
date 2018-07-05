def deco(func):
	print("=========")
	return func

@deco #test = deco(test)先把test传入func，然后deco执行完了后返回func，再运行test()
def test():
	print("test函数运行")
res1 = test()
print(res1)


# def deco(func):
# 	print("=========")
# 	return func

# @deco  #Foo = deco(Foo)
# class Foo():
# 	pass
# f1 = Foo()
# print(f1)

# def deco(obj):
# 	print("=======",obj)#这里的obj可以看作Foo
# 	obj.x = 1#然后操作这个类，赋值
# 	obj.y = 2
# 	obj.z = 3
# 	return obj
# @deco #Foo=deco(Foo)
# class Foo():
# 	pass
# f1 = Foo()
# print(f1)