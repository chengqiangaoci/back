#递归函数
def test(n):
	Print(n)
    test()

test(10)#这就是无限循环

#只要函数自己在自己内部调用自己，就是递归
#递归条件：为避免死循环，一定要有约束条件
def test(n):
	print(n)
	if int(n/2) ==0:
		return n
	return test(int(n/2))
