#数字

#转换进制
# num = "a"
# jinzhi = int(num,base=16)#转换为16进制
# print(jinzhi)


#字符串1
# name = "chengqian"
# print(name.upper())#全部大写
# print(name.lower())#全部小写
# print(name.capitalize())#首字母大写

#计数
# test1 = name.count("c",5,6) #计算c字符出现的次数，在位置5-6之间
# print(test1)

#结尾
# test2 = name.endswith("x")#是否以x结尾
# print(test2)

#开头
# test3 = name.startswith("x")#是否以x开头
# print(test3)

#查找
# name = "chengqian"
# test4 = name.find("ch")#查找ch在什么位置
# print(test4)
# test5 = name.find("ch",5,7)#在5-7位置找，没找到的话显示-1
# print(test5)

#替换
# test6 = "i am {0},age{1}"
# v = test6.format("chengqian",26)#替换为chengqian和26
# print(v)

#是否只包括
# test7 = name.isalnum()#是否只包含字母和数字
# print(test7)

#是否是字母
# test = "chengqiangaoci"#汉字也算
# test1 = test.isalpha()#是否是字母
# print(test1)

#是否是数字
# test2 = "②"
# v1 = test2.isdecimal()#支持数字123之类的
# v2 = test2.isdigit()#支持数字123，包括各种类型的，②，二
# v3 = test2.isnumeric()#支持以上的，并且包括“二”，还有字节
# print(v1,v2,v3)

#是否可打印
# test = "chengqian\nchengqian"
# test1 = test.isprintable()#是否可打印，当字符串里存在不可见的东西（\n或者\t时），false
# print(test1)

#是否全空格
# test = "            "
# test1 = test.isspace()#是否字符串里是否全部！是空格
# print(test1)

#是否是标题
# test = "cheng qian"
# test1 = test.title()#转换为标题，即首字母都是大写
# test2 = test.istitle()#判断是否是标题，即所有的首字母都是大写
# print(test1,test2)

#非常重要的！！！！！！！！！！！！！！
# test = "你是风儿我是沙"
# test2 = " ".join(test)#将字符串中的每个元素按照指定分隔符进行拼接
# print(test2)

#批量添加
# test = "cheng"
# test1 = test.ljust(1,'*')#在字符串右边+1个*
# test2 = test.rjust(5,'*')#在字符串左边+5个*
# test3 = test.center(5,"*")#左右都加5个*
# print(test1)
#print(test2)

#删除空格
# test = " chengqian "
# test1 = test.lstrip()#去掉左边的空格、换行\n和\t 
# test2 = test.rstrip()
# test3 = test.strip()
#test = test.lstrip("c") #也可以去掉左边的字符
# print(test1,test2,test3)

#分割
# test = "chengqian"
# # test1 = test.partition("n")#只能分割第一个n，分成三份
# # test2 = test.rpartition("n")#从右边开始分割
# test3 = test.split("n",2)#分割成三份，但是没有n，然而可以分割多次（看参数）
# # test4 = test.rstrip("n")#从右边开始分割成一份，但是没有n
# print(test3)

#按行分割
# test = "chengqian\ngaoci\ndabaitu"
# test1 = test.splitlines(True)#按行分割，加参数true的话，换行符的话也包含，
# print(test1)

#大小写互换
# test = "ChengQian"
# test1 = test.swapcase()#大写变成小写，小写变成大写
# print(test1)

#字符长度
# test = "程前"
# test1 = "chengqian"
# print(len(test))#获取字符数
# print(len(test1))
test = [1,11,111,"abc"]
print(len(test))#在列表中就是以逗号间隔来算

#s索引
# test = "你叫的小闲"
# for i in test:
# 	print(i)
#还有另外一种写法
# test = "你叫的小闲"
# index = 0
# while index < len(test):
# 	print(test[index])
# 	print("========")
# 	index += 1

# test = "chengqian"
# test1 = test.replace("n","bbbbb",1)#后面没参数就是所有的n都替换，有参数就替换参数次
# print(test1)

#索引的快速用法
# a,b,c = "hee"
# print(a,b,c)
a,*b,c = "hoahflahwrwqupjalsdj"
print(b)
print(a,c)#这样就可以很方便的取头尾















