#map接受两个参数，一个是函数，一个是iterable
L = [1,2,3,4,5,6,7,8,9]
def test(i):
	return i*i
r = map(test,L)#这是一个迭代器
print(list(r))