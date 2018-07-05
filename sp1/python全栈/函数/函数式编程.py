#面向过程编程
#函数式编程：不用变量保存状态，不修改变量

#面向过程
# a = 1
# def test1():
# 	global a
# 	a += 1
# 	return a
# print(test1())
# print(a)

#函数式编程：经常使用递归，
# n = 1
# def test1():
# 	return n+1 #这里没有过程，不修改变量，不用变量保存状态
# print(test1())
# print(n)

#函数式编程：将函数当参数传递
# def foo(n):
# 	print(n)
# def foo1(name):
# 	print("my name is %s" %name)
# foo(foo1("chengqian"))#这里只打印下面的，另外一个会是none

# def foo():
# 	print("111")
# 	return foo()
# foo()#无限循环


#map接受两个参数，一个是函数，一个是iterable
# L = [1,2,3,4,5,6,7,8,9]
# def test(i):
# 	return i*i
# r = map(test,L)#这是一个迭代器
# print(list(r))

#filter函数与map函数类似，但是它是根据返回值是true还是false决定保留与否
# def odd(n):
# 	return n%2 == 1
# print(list(filter(odd,[1,2,3,4,5,6,7])))

#reduce在python3中在模块中 
from functools import reduce
#reduce把一个函数作用在一个列表上，这个函数必须接收两个参数
#reduce把结果继续和序列的下一个元素做累积计算
# def add(x,y):
# 	return x + y
# reduce(add,[1,3,4,5,6,7])#累计相加，结果是26
#以上这个函数可以使用sum，但是如果想变成134567这个数的话
def add(x,y):
	return x*10 + y
print(reduce(add,[1,3,4,5,6,7]))
