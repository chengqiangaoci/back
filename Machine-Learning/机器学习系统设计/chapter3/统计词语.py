import os
from sklearn.feature_extraction.text import CountVectorizer
dir = "C:/Users/Administrator/Desktop/机器学习/机器学习系统设计/chapter3/data"
posts = [open(os.path.join(dir,f)).read() for f in os.listdir(dir)] #获取文件目录及文件内容

import nltk.stem
english_stemmer = nltk.stem.SnowballStemmer("english")
class StemmedCountVectorizer(CountVectorizer):
	def build_analyzer(self):
		analyzer = super(StemmedCountVectorizer,self).build_analyzer()
		return lambda doc:(english_stemmer.stem(w) for w in analyzer(doc))
vect = StemmedCountVectorizer(min_df=1,stop_words="english")

#fit_transform是拟合以及标准，而transform是标准化，并且因为前面已经fit过了，所以后面只用标准化
x_train = vect.fit_transform(posts)
num_samples,num_features = x_train.shape
print(num_samples,num_features)
print(x_train)
print(x_train.todense())#向量化，也是最重要的
print(vect.get_feature_names())#获取所有词粒

#新帖子向量化
new_post = "imaging databases"
new_post_vec = vect.transform([new_post])
print(new_post_vec.todense())


#计算欧式距离
import scipy as sp
def dist_norm(v1,v2):
	v1_normalized = v1/sp.linalg.norm(v1.toarray())
	v2_normalized = v2/sp.linalg.norm(v2.toarray())
	delta = v1_normalized - v2_normalized
	print(delta.todense())
	print("1=================")
	print(v1_normalized.todense())
	print("-------------------")
	print(v2_normalized)
	return sp.linalg.norm(delta.todense())#norm计算欧几里得范数

import sys
best_doc = None
best_dist = sys.maxsize#最大的int值
print("best_dist is :============" + str(best_dist))
best_i = None
for i in range(0,num_samples):
	post = posts[i]
	if post == new_post:
		continue
	post_vec = x_train.getrow(i)#返回第一行
	d = dist_norm(post_vec,new_post_vec)
	print("===post %i with dist=%.2f:%s"%(i,d,post))
	if d < best_dist:
		best_dist = d
		best_i = i
print("Best post is %i with dist=%.2f"%(best_i,best_dist))








