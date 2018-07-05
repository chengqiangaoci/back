#迭代器协议：对象必须提供一个next方法，要么返回迭代下一项，要么报错
class Foo():
	def __init__(self,n):
		self.n = n
	def __iter__(self):#这样的话，实例变成可迭代
		return self
	def __next__(self):#调用next来返回值
		self.n+=1
		return self.n
f1 = Foo(10)
print(f1.__next__())
print(next(f1))#跟上面一样
for i in f1:#f1.__iter__() == iter(f1)
	print(i)