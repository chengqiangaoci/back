#要考虑同义词的影响，如something is good/something is not bad意思是一样，但词性有所不同

#通过nltk的超级的超级大字典分析本文内容，帮助人们寻找单词的含义，nltk的一个基本功能就是识别句子中各个词的词性：
# from nltk.book import *
# from nltk import word_tokenize
# text = word_tokenize("Strange women lying in ponds distributing swords is no basis for a system of government.Supreme executive power derives from a mandate from the masses,not from some farcical aquatic ceremony")
# from nltk import pos_tag#每个单词背分开放在一个元组中，一边是单词，一边是nltk的词性识别。
# print(pos_tag(text))#得到的结果就是对每个单词的词性分析，词性的来源是Penn Treebank标记表

#nltk使用英语的上下文无关文法（cntext-free grammmar)识别词性，即使用一个规则集合，用一个有序的列表确定一个词后面可以跟哪些词性。

#应用领域：如，采集网站文字后，可能想从文字中搜索Google，但只想要动词而不是专业名词的google
from nltk import word_tokenize,sent_tokenize,pos_tag
#sent_tokenize是对文本按照句子分割，word_tokenize是对句子进行分词
sentences = sent_tokenize("Google is one of the best companies in the world. I constantly google myself to see what I'm up to")#注意英文中，每个.后面要空格才算是另外一个句子
nouns = ["NN","NNS","NNP","NNPS"]#Penn Treebank标记表

for sentence in sentences:
	if "google" in sentence.lower():
		taggedWords = pos_tag(word_tokenize(sentence))
		for word in taggedWords:
			if word[0].lower() == "google" and word[1] in nouns:
				print(sentence)#打印google作为名词的句子


































