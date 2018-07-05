#eval可以将字符串数据转换为其他类型的数据

#字符串转换为列表
test = "[13,4,5,6]"
print(type(test))
test1 = eval(test)
print(type(test1))
print(type(test))

