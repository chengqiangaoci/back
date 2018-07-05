#斐波那契数列：后面的数前两个数之和：1、1、2、3、5、8
class Fibl():
	def __init__(self):
		self._a = 1
		self._b = 1
	def __iter__(self):
		return self
	def __next__(self):
		self._a,self._b = self._b,self._a + self._b 
		return self._a
f1 = Fibl()
# print(next(f1))
# print(next(f1))
# print(next(f1))
# print(next(f1))
for i in f1:
	if i < 100:
		print(i)