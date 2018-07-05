#字符匹配：普通字符和字母都会和自身匹配，主要学习的就是元字符
#遵循贪婪匹配：有多少个就匹配多少个
#贪婪匹配改成惰性匹配，后面加?

# .点是通配符，什么都可以代替(除了\n)
import re
# test = re.findall("alex","adsfaeyxsklg")#两个参数，匹配规则与内容(字符串)
# print(test)

# test1 = re.findall("a..x","adsfaeyxsklg")
# print(test1)

# ^从开头进行匹配,也只匹配开头的那个序列
# test2 = re.findall("^a..x","adsfaeyxsklg")
# print(test2)

# $以什么结尾，也只匹配结尾的那个序列
# test3 = re.findall("s..g$","adsfaeyxsklg")
# print(test3)

#重复符号：*+?{}
# *紧挨着的那个字符重复 0-∞次
# test4 = re.findall("ed*","adsfaeddddddddddyxsklg")
# print(test4)
# test5 = re.findall("^d*","dddgasafasfdddddd")
# print(test5)

# +重复1-∞次
# test6 = re.findall(".lex+","asafsasfalexxx")
# print(test6)

#? 重复0-1次
test7 = re.findall(".lex?","asafsasfalexxx")#只能取一个
print(test7)

# {} 想重复多少次都可以，{6}重复六次
test8 = re.findall("alex{3}","asafsasfalexxx")#重复三次
print(test8)



#[]字符集,在字符集里没有特殊符号,除了 - ^ \
test = re.findall("x[y,z]p","xpyxypdsdsxzpdsdx,p")
print(test)

test = re.findall("q[a-z]","quo")
print(test) 

test = re.findall("q[a-z]*","qcfasfjwhrjawhrawf")
print(test)

test = re.findall("q[^a-z]","q231")#这个^的意思非a-z
print(test)

# test = re.findall("\([^()]\)","12+(34*6+2-5*(2-1))")
# print(test)


#元字符之转义符\
#\d匹配任何十进制数，相当于[0-9]
#\D 相当于[^0-9]
#\s匹配任何空白字符，[\t\n\r\f\v]
#\S匹配任何非空白字符，[^\t\n\r\f\v]
#\w匹配任何字母数字字符 [a-zA-Z0-9]
#\W匹配任何非字母数字字符 [^\a-zA-Z0-9]
#\b匹配一个特殊字符便签，比如空格，&,#等

# test = re.findall("^I.","I am LIST")#空格怎么弄？
# print(test)

# test = re.findall("I\\b","hello I am LIST")#python中\b有原本意思
# print(test)
test1 = re.findall(r"I\b","hello I am LIST")#这个r的意思是说这个内容符合re
print(test1)

test = re.findall(r"c\\l","abc\ledasd")#出来的结果包括python转义的结果
print(test)



# | 二选
test = re.findall(r"ka|b","sdjkakabsf")
print(test)


#()分组处理
# test = re.findall("(abc)+","abcabcabcacc")
# print(test)#优先取组里面的内容，也就是一个abc
# test = re.findall("(?:abc)","abcabcabc")
# print(test)#取消组里面的优先级

#search只会找一个匹配的内容
test11 = re.search("\d+","sdaf34sfaf15")
print(test11)#显示索引和匹配和结果的内容

#取得结果
test = re.search("\d+","sdaf34sfaf15").group()
print(test)

#挺重要的分组
# test = re.search("(?P<name>[a-z]+)\d+","sdaf34sfaf15").group("name")
# print(test)

#给数字分组
# test = re.search("(?P<name>[a-z]+)(?P<age>\d+)","sdaf34sfaf15").group("age")
# print(test)


#match只会从开头匹配，也就是search加一个^
test = re.match("\d+","2fashfkas33fjasljf22kjdlsajd113").group()
print(test)

#split分割
test = re.split(" ","2fashf kas33fja sljf22kjdlsajd113")
print(test)

#sub替换
# test = re.sub("\d","abc","alv6in5yuan6")
# print(test)

#compile编译
test = re.compile("\\W*")#规则已经编译好了
test1 = test.split("M.L")
print(test1)

#finditer迭代,把所有的结果封装到迭代器，返回一个迭代器对象
# test = re.finditer("\d","dasdasd23")
# print(test)
# for i in test:
# 	print(i.group())


#findall会优先选取分组的内容
# test = re.findall("www\.(baidu|163).com","www.baidu.com")
# print(test)#这里只会打印baidu

#去掉优先级
# test = re.findall("www\.(?:baidu|163).com","www.baidu.com")
# print(test)#这里只会打印全部



