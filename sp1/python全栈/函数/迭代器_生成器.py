#递归就是自己调用自己，迭代是使用for循环遍历

#迭代器协议：对象必须提供一个next方法，执行该方法要么
#返回迭代中的下一项，要么错误以终止迭代。

#可迭代对象：实现了迭代器协议的对象（对象内部定义__iter__()方法）

#字符串列表元组字典集合文件对象都不是迭代器，只不过在for
#循环的时候调用他们内部的__iter__方法，把他们变成了迭代器

# 凡是可作用于for循环的对象都是Iterable类型；
# 凡是可作用于next()函数的对象都是Iterator迭代器类型，它们表示一个惰性计算的序列；
# 集合数据类型如list、dict、str等是Iterable可迭代对象但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。



#生成器是一种数据类型，自动实现迭代器协议，因此也是可迭代对象
#生成器分类及在python中的表现形式
#1.常规函数定义，如yield函数
#2.类似于列表推导，但是返回按需产生结果的一个对象
# def test():
# 	yield 1#生成器

# print(test())#打印的是生成器

# for i in test():
# 	print(i)#这里打印出1,把生成器迭代出来

# g = test()
# print(g.__next__())#这里也打印出来了1

# #三元表达式
# test = ["鸡蛋%s" %i for i in range(10) if i > 5]
# print(test)


#生成器表达式
# test = sum(x**2 for x in range(4))
# print(test)

#生成器是（）而不是[]
# test1 = ("鸡蛋%s" %i for i in range(10))
# print(test1)#打印了一个生成器
# print(test1.__next__())#一个个打印目标
# print(next(test1))

#生成器的优势：节约内存等

# test = (i for i in range(10))#生成器表达式
# print(test)#打印的生成器

# test1 = [i for i in range(10)]#列表生成器
# print(test1)


#效率高，占内存小
# def xiadan():
# 	for i in range(10000):
# 		yield "鸡蛋%s" %i
# test = xiadan()
# test1 = test.__next__()
# test1 = test.__next__()
# test1 = test.__next__()
# test1 = test.__next__()
# print("取鸡蛋",test1)


#send的用法
def f():
	print("ok")
	s = yield 6
	print(s)
	print("ok2")
	yield 3

g = f()
test = next(g)
print(test)#将yield的值打印出来
g.send(5)#重新复制给第一个yield，所以会打印出5







