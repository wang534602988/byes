#主程序
'''
1从分词文档和类型文档读取数据，转化为列表
2将数据分为数据集和测试集
3创建词典
4生成词向量
5计算概率并比较
6计算准确率
'''
import numpy as np
from numpy import *
import random

#变量准备工作
allcontent = []  # 保存所有文本列表的列表
allcla = []  # 保存文本类型的列表
punctuation = '!,;:?"\'、，； 。 : ：？！1234567890'  # 停用词
path = 'G:/学习/大三上/文本分析/test/'#文件路径

#读取文件生成分词列表与分类列表
with open(path + 'classtag.txt', 'r', encoding='utf-8', errors='ignore') as jo:
	cla = jo.read()
	for i in range(len(cla)):
		try:
			allcla.append(int(cla[i]))
		except:
			0
with open(path + 'data.txt', 'r', encoding='utf-8', errors='ignore') as jo:
	data = jo.read()
content0 = data.split('2')
for line in content0:
	alist = line.split('1')
	allcontent.append(alist)

# 生成训练集与测试集
def randspl(data, cla):
	dataDig = []
	claDig = []
	for i in (range(int(len(cla) / 2))):
		random.seed(i)
		rd = random.randint(0, int(len(cla) - 1))
		dataDig.append(data[rd])
		data.pop(rd)
		claDig.append(cla[rd])
		cla.pop(rd)
	return data, cla, dataDig, claDig


# 创建所有文件的不重复词构成的词典
def creatVec(dataSet):
	vocabSet = set([])
	for document in dataSet:
		vocabSet = vocabSet | set(document)
	return list(vocabSet)


# 建立文本向量
def set2Vec(vocabList, inputSet):
	returnVec = [0] * len(vocabList)
	for word in inputSet:
		if word in vocabList:
			returnVec[vocabList.index(word)] = 1
		else:
			0
	return returnVec


# 根据文本向量训练模型
def train(matrix, category):
	vect1, vect2, vect3, vect4, vect5 = [], [], [], [], []
	vect = [vect1, vect2, vect3, vect4, vect5]
	p = [0, 0, 0, 0, 0]
	classCount = [0, 0, 0, 0, 0]
	count = len(category)
	for i in range(count):
		index = category[i]
		classCount[index - 1] = classCount[index - 1] + 1
		vect[index - 1].append(matrix[i])
	for i in range(len(p)):
		p[i] = classCount[i] / count
	return vect, p


# 计算并分类
def classifyNB(testVec, classVec, pList):  # 比较概率大小进行判断，
	tMat = np.mat(testVec).T
	classMat = []
	for vec in classVec:
		classMat.append(np.mat(vec))
	p1 = log(sum((classMat[0]* tMat)+1)/len(classMat[0])) + log(pList[0])
	p2 = log(sum((classMat[1] * tMat) + 1) / len(classMat[1])) + log(pList[1])
	p3 = log(sum((classMat[2] * tMat) + 1) / len(classMat[2])) + log(pList[2])
	p4 = log(sum((classMat[3] * tMat) + 1) / len(classMat[3])) + log(pList[3])
	p5 = log(sum((classMat[4] * tMat) + 1) / len(classMat[4])) + log(pList[4])
	pclass = {1: p1, 2: p2, 3: p3, 4: p4, 5: p5}
	return sorted(pclass.items(),key=lambda i:i[1],reverse=True)[0][0]


# 测试
def test():
	content, cla, testword, testcla = randspl(allcontent, allcla)#训练文本，训练类型记录，测试文本，测试类型记录
	dictList = creatVec(content)#不重复词词典
	wordVec = []#训练文本分词集
	for oneTxt in content:
		wordVec.append(set2Vec(dictList, oneTxt))
	vect, p = train(wordVec, cla)#获取训练文本向量与类型概率
	testlens = len(testcla)#获取测试集数量
	gettag = 0#记录成功命中数量
	for i in range(testlens):
		testVec = set2Vec(dictList, testword[i])#生成测试集向量
		testClass = classifyNB(testVec, vect, p)#得到预测类型
		print(testClass,testcla[i])
		if testClass == testcla[i]:#准确率统计
			gettag = gettag + 1
	prect = gettag / testlens
	return prect
print(test())
