#      D
#   B
#A        F
#   C
#      E
#BC继承A，DE分别继承BC，F继承DE
#新式继承：广度优先D、B,然后E、C,最后才是A
class A():
	def test(self):
		print("A")
class B(A):
	def test(self):
		print("B")
class C(A):
	def test(self):
		print("C")
class D(B):
	def test(self):
		print("D")
class E(C):
	def test(self):
		print("E")
class F(D,E):#不论别的，这里先继承D
	def test(self):
		print("F")
f1 = F()
f1.test()#打印F
print(F.__mro__)#这样也可以查看继承顺序