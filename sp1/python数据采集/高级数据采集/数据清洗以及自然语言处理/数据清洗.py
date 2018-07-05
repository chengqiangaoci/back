#编写代码清洗数据
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
from collections import OrderedDict

def cleanInput(input):
    input = re.sub('\n+', " ", input)#换行符替换为空格
    input = re.sub('\[[0-9]*\]', "", input)#
    input = re.sub(' +', " ", input)#连续空格替换为一个空格
    input = bytes(input, "UTF-8")#将内容转换为UTF格式
    input = input.decode("ascii", "ignore")#转义字符因为不能被ascii decode，如果不加ignore就会报错，加了ignore就会被忽略，这一行用来消除转义字符
    cleanInput = []
    input = input.split(' ')
    for item in input:
        item = item.strip(string.punctuation)#括号里用于获取所有的标点符号，这整条函数式为了消除所有标点符号
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):#剔除单字符的单词，除非这个字符是i或者a
            cleanInput.append(item)
    return cleanInput

def getNgrams(input, n):
    input = cleanInput(input)
    output = dict()
    for i in range(len(input)-n+1):
        newNGram = " ".join(input[i:i+n])
        if newNGram in output:
            output[newNGram] += 1
        else:
            output[newNGram] = 1
    return output

html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BeautifulSoup(html, "html.parser")
content = bsObj.find("div", {"id":"mw-content-text"}).get_text()

ngrams = getNgrams(content, 2)
ngrams = OrderedDict(sorted(ngrams.items(), key=lambda t: t[1], reverse=True))
print(ngrams)