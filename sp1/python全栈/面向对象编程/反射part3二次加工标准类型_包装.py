##包装一个类型通常是对已存在的类型的一些定制，这些方法可以新建修改或删除现有产品的功能，其他的保持原样
# class List(list):#继承python内置类list
# 	pass
# l1 = List("hello world")#使用内置类将其列表化
# print(l1)
# l2 = list("hello world")#与l1相同


# class List(list):
# 	def show_middle(self):#去中间的字符
# 		mid_inde = int(len(self)/2)
# 		return self[mid_inde]
# p1 = List("helloworld")
# print(p1.show_middle())


# class List(list):
# 	def append():
# 		pass
# 	def show_middle(self):#去中间的字符
# 		mid_inde = int(len(self)/2)
# 		return self[mid_inde]

# l1 = List("helloworld")
# l1.append(111111)#因为上面定制了append，所以这里的处理遵循上面的函数而不是内置函数


#定制功能，append只对字符串起作用
class List(list):
	def append(self,p_object):#p_object相当于上面的111111
		if type(p_object) is str:
			#self.append(p_object)这样会陷入递归
			list.append(self,p_object)
			#super().append(p_object)#跟上面的一样

l1 = List("hello world")
l1.append("SB")
print(l1)





