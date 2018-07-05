#set和dict类似，但是不储存value
#要创建一个set，首先要提供一个list作为输入集合

#list中的重复元素会被过滤
test = set([1,1,1,1,1,3,4,5,6,7])
print(type(test))

#列表删除使用pop,del,添加使用append,替换replace
#字典删除使用pop
#set使用add添加，remove删除