import operator
from os import *
import numpy as np
trainingFileList = listdir('trainingDigits')
	#返回文件夹下文件的个数
m = len(trainingFileList)
trainingMat = np.zeros((m, 1024))
print(trainingMat)