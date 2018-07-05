#纯文本
# import requests
# textPage = requests.get("http://www.pythonscraping.com/pages/warandpeace/chapter1.txt")
# print(textPage.text)


#读取CSV文件
import requests
from io import StringIO
import csv
data = requests.get("http://pythonscraping.com/files/MontyPythonAlbums.csv").text
dataFile = StringIO(data)
csvReader = csv.reader(dataFile)

for row in csvReader:
	print("The album \""+row[0]+"\" was released in "+str(row[1]))