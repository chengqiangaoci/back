import numpy as np
test = open("datingTestSet.txt")
arrayOLines = test.readlines()
numberOfLines = len(arrayOLines)
print(numberOfLines)
returnMat = np.zeros((numberOfLines,3))
index = 0
for line in arrayOLines:
		#s.strip(rm)，当rm空时,默认删除空白符(包括'\n','\r','\t',' ')
		line = line.strip()
		print(line)
		#使用s.split(str="",num=string,cout(str))将字符串根据'\t'分隔符进行切片。
		listFromLine = line.split('\t')
		returnMat[index,:] = listFromLine[0:3]
		print(returnMat)