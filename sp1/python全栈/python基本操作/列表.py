#列表支持切片

#支持for循环，但是结果不是列表
# test = [1,2,3,["chengqian","shenyue"]]
# for i in test:
# 	print(i)
# 	print(type(i))

#对列表进行修改
# test = [1,2,3,"chengqian","shenyue"]
# test[1] = ["dabaitu",["gaoci"]]#修改对应位置
# print(test)

#删除列表
# test = [1,2,3,"chengqian","shenyue"]
# del test[1]
# print(test)

#列表转换为字符串，需要自己写一个for循环（在列表中既有数字也有字符串时）
# s = ""
# test = [1,2,3,"chenqgian"]
# for i in test:
# 	s = s + str(i)
# print(s)

#列表的修改值不能新增一个变量等于，只需要test.xx()就行了
# test = [1,2,3,"chenqgian"]
# test1 = test.append(5)
# print(test1)#这时候显示的是none，因为值在test里
# print(test)#这个才是想要的结果

#清空
# test = [1,2,3,"chenqgian"]
# test.clear()#将列表里的内容清空
# print(test)

#复制
# test = [1,2,3,"chenqgian"]
# test1 = test.copy()#复制的意思
# print(test1)

#计数
# test = [1,2,2,3,"chenqgian"]
# test1 = test.count(2)#计算出现的次数
# print(test1)

#添加
# test = [1,2,3,"chenqgian"]
# test.extend([9898,"budeliao"])#append是把后面当一个整体，而这个是分别传，没有列表。
# print(test)

#索引
# test = [1,2,3,"chenqgian"]
# test1 = test.index(2) #只找元素第一次出现的索引
# print(test1)

#插入
# test = [1,2,3,"chenqgian"]
# test.insert(2,"gaoci") #指定位置插入，
# print(test)

#删除并显示
# test = [1,2,3,"chenqgian"]
# #可以获取到删除的值
# test1 = test.pop()#这里显示的是被删除的值
# print(test)#这里是原值
# test2 = test.pop(1)#删除指定位置的值

# test = [1,2,2,3,"chenqgian"]
# test1 = test.remove(2) #左边优先,与pop不同的是被删除的值不会显示
# print(test)

#排序:可以接收函数
# test = [4,2,3]
# test.sort()#排序
# test.sort(reverse=True)#倒过来
# print(test)
#sorted([1,3,4],key=abs)#绝对值
#key=str.lower:忽略大小写排序，否则大写会在小写前面











