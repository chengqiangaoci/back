L = [x*x for x in range(10)]
print(L)
#结果是一个列表

G = (x*x for x in range(10))
#print(G)
#结果是<generator object <genexpr> at 0x0000000002669FC0>
#要想获取G元素，可以使用next（G）
for i in G:
	print(i)
