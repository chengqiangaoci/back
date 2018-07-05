#集合由无序不同元素、不可变类型组成【只能存放数字、字符串和元组】
# s = {1,2,3,4,5,6}#因为集合是不同元素，所以会去重

# test = set("hello")
# print(test)#结果是一个个单独的字符，并且不重复

#生成集合
# test = set(["chengqian"])#生成集合。这里可以是列表
# print(test)

#添加
# test = {1,2,3,4,5,6}
# test.add("s")#也是末尾添加,这里也不用添加新的变量，不然输出为None
# print(test)

#清空和赋值
# test = {1,2,3,4,5,6}
# test.clear()#清空
# print(test)
# test1 = test.copy()#复制
# print(test1)

#test = {1,2,3,4,5,6}
# test.pop()#随机删除
# test.remove(6)#指定删除元素，不存在的话会报错
# print(test)
#test.discard(7)#删除指定元素，但是不存在的话不会报错
#print(test)

#寻找交集↓
# python_1 = ["chengqian","dabaitu","gaoci"]
# python_2 = ["chengqian","gaoci","shenyue"]
# python = []
# for i in python_2:
# 	if i in python_1:
# 		python.append(str(i))
# print(python)

#寻找交集2
# python_1 = ["chengqian","dabaitu","gaoci"]
# python_2 = ["chengqian","gaoci","shenyue"]
# python1 = set(python_1)
# python2 = set(python_2)
# print(python1.intersection(python2))#交集
# print(python1&python2)#交集
# print(python_1&python_2)#这个会报错

#并集1
# python_1 = ["chengqian","dabaitu","gaoci"]
# python_2 = ["chengqian","gaoci","shenyue"]
# python = python_1 + python_2
# test = set(python)
# print(test)

#并集2
# python_1 = ["chengqian","dabaitu","gaoci"]
# python_2 = ["chengqian","gaoci","shenyue"]
# python1 = set(python_1)
# python2 = set(python_2)
# print(python1|python2)#并集
# print(python1.union(python2))#并集

#差集1
python_1 = ["chengqian","dabaitu","gaoci"]
python_2 = ["chengqian","gaoci","shenyue"]
python1 = set(python_1)
python2 = set(python_2)
print(python1-python2)#差集
print(python1.difference(python2))#差集

#交叉补集：删去共有的部分
# python_1 = ["chengqian","dabaitu","gaoci"]
# python_2 = ["chengqian","gaoci","shenyue"]
# python1 = set(python_1)
# python2 = set(python_2)
# print(python1.symmetric_difference(python2))#交叉补集
# print(python1^python2)#交叉补集

#差集后更新
# python_1 = ["chengqian","dabaitu","gaoci"]
# python_2 = ["chengqian","gaoci","shenyue"]
# python1 = set(python_1)
# python2 = set(python_2)
# print(python1.difference_update(python2))#就是将原有的python1更新
# print(python1)

#是否有交集
# python_1 = ["chengqian","dabaitu","gaoci"]
# python_2 = ["chengqian","gaoci","shenyue"]
# python1 = set(python_1)
# python2 = set(python_2)
# print(python1.isdisjoint(python2))

#是否是子集
# python_1 = ["chengqian","gaoci"]
# python_2 = ["chengqian","gaoci","shenyue"]
# python1 = set(python_1)
# python2 = set(python_2)
# print(python1.issubset(python2))#python1是否是python2的子集

#是否是父集
# python_1 = ["chengqian","gaoci"]
# python_2 = ["chengqian","gaoci","shenyue"]
# python1 = set(python_1)
# python2 = set(python_2)
# print(python2.issuperset(python1))#python2是否是python1的父集

#update与union
python_1 = ["chengqian","dabaitu","gaoci"]
python_2 = ["chengqian","gaoci","shenyue"]
python1 = set(python_1)
python2 = set(python_2)
# python1.update(python2)#这个已经赋予给了python1，更新多个值
# print(python1)#合并
# python1.union(python2)#这个还没有合并到python1，不更新
# print(python1)
# python1.add(1)#这个已经赋予给python1，只更新一个值
# print(python1)


#集合set一般都是可变的，但是也可以变成不可变
# s = frozenset("hello")#这样就是不可变


#最后一个小窍门，如果相对简单列表去重
# test = ["1","1",2,2,3,3]
# test1 = list(set(test))#这样就对列表去重了
# print(test1)























