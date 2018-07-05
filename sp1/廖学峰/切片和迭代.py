#针对于元组和列表
#[:3]=[0:3]
#每两个取一个[10:20:2]
#复制[:]

#字符串也可以看成一种list，每个元素就是一个字符

#enumerate函数可以将list编程索引-元素对
for i,value in enumerate(["A","B","C"]):
	print(i,value)
	#结果是0 A
    #      1 B
    #      2 C

#