# import nltk
# nltk.download()
#以上这个是初始化安装包，用一次就行了。

#使用NLTK做统计分析一般是从Text对象开始
# from nltk import word_tokenize
# from nltk import Text
# tokens = word_tokenize("Here is some not very interesting text")#将字符串分解为单个字符
# text = Text(tokens)


# from nltk.book import * #加载所有书
# print(len(text6)/len(words))


#将文本对象放到频率分布对象FreqDist中，查看哪些单词最常用，以及单词的频率
from nltk.book import text6
from nltk import FreqDist
f = FreqDist(text6)
# print(f.most_common(10))#most_common以降序返回，参数代表多少个



#使用nltk可以非常轻松地创建并搜索一个2-garm模型
# from nltk.book import *
# from nltk import FreqDist
# from nltk import bigrams #2-gram在nltk中称为bigrams
# bigrams = bigrams(text6) #创建了2-gram
# bigramDist = FreqDist(bigrams) #频率
# print(bigramDist[("Sir","Robin")])#为了匹配2-grams，要将sir Robin分解成一个数组，如括号里



#一般情况下不是2-grams，因此大多数情况下可以导入ngrams模块
# from nltk import ngrams
# from nltk.book import *
# from nltk import FreqDist
# f = ngrams(text6,4)#4-grams
# fd = FreqDist(f)
# print(fd[("father","smelt","of","elderberries")])

#频率分布、文本对象和n-grams整合在循环中进行迭代：如打印文本中以cocount开头的4-grams序列
# from nltk.book import *
# from nltk import ngrams
# fs = ngrams(text6,4)#实质上是个生成器
# for f in fs:
# 	if f[0] == "coconut":
# 		print(f)























