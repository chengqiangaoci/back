# def deco(obj):
# 	obj.x = 1#给类增加数据属性
# 	obj.y = 2
# 	obj.z = 3
# 	return obj
# @deco
# class Foo():
# 	pass
# f1 = Foo()
# print(f1.x)


#可以自定义类的属性
def Typed(**kwargs):
	def deco(obj):
		obj.x = 1#给类增加数据属性
		obj.y = 2
		obj.z = 3
		return obj
	return deco
@Typed(x=1,y=2,z=3)#这个语法糖本身就会运行参数，可以自定义类的属性
class Foo():
	pass














