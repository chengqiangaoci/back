#filter函数与map函数类似，但是它是根据返回值是true还是false决定保留与否
def odd(n):
	return n%2 == 1
print(list(filter(odd,[1,2,3,4,5,6,7])))

#sorted函数可以进行排序，并可以接受一个key函数返回的结果进行排序
print(sorted([1,-222,123],key=abs))