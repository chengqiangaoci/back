#slots的初衷是为了优化内存
#dict每个实例都会占有内存
#slots会为实例使用一种更为紧凑的内部表示——呵哦小的固定大小的数组
#坏处是不能再给实例添加新的属性，只能使用在slots中定义的那些属性名
#每一个属性都不能使用__dict__，因为已经不是字典了
# class Foo():
# 	#__slots__=["name","age"]#定义了两个key
# 	__slots__ = "name"
# f1 = Foo()
# f1.name="chengqian"
# print(f1.name)
# print(f1.__slots__)
# f1.age = 18#这里就不能定义了，因为上面slots就定义了一个key


#doc无法继承给子类
# class Foo():
# 	"描述信息"
# 	pass
# class Bar(Foo):
# 	pass
# print(Bar.__doc__)#子类不能继承父类的
# print(Foo.__dict__)#Foo有doc字典信息


#查看实例xx来自于哪个模块：print(xx.__module__)
#查看实例xx来自于哪个类：print(xx.__class__)

