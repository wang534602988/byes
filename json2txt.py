#将json文件整理转化为txt文件
'''
从chinese-poetry-master文件夹中选取了部分诗、词、文言文数据，
并将json文件转为txt文件与新闻和论文的txt文件格式统一，
其中主要的问题是文言文数据量相对较少，可能会影响到计算结果
'''
import json
import os

#处理函数，参数分别为文件路径，关键字，保存文件名
def json2txt(path, key, textName):
	fileList = os.listdir(path)
	shi = ()
	for fileName in fileList:
		if fileName.find('.json') != -1:
			with open(path + '\\' + fileName, 'r', encoding="utf-8") as jo:
				info = json.load(jo)
			if isinstance(info, list):
				for line in info:
					try:
						poet = tuple(line[key])
						shi = shi + poet + tuple('\n')
					except:
						print("json文件格式不符合要求")
	txt = ''.join(shi)
	f = open(path + '\\' + textName, "w", encoding='utf-8')
	f.write(txt)
	f.close()

#主函数,将文言文、诗、词转为txt
json2txt('G:\学习\大三上\文本分析\文言文', "paragraphs", '文言文.txt')
json2txt('G:\学习\大三上\文本分析\shi', "paragraphs", 'shi.txt')
json2txt('G:\学习\大三上\文本分析\ci', "paragraphs", 'ci.txt')
print("1")
