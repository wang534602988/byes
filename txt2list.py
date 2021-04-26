# 分词部分
'''
分词部分是通过txt文件形成分词列表和对应的类型列表，其中
shi：1
ci：2
文言文：3
新闻：4
期刊论文：5
以便之后使用，存放到data.txt和classtag.txt文件中，分词列表用1和2分割
'''
import re
from numpy import *
import random
import time

punctuation = '!,;:?"\'、，； 。 : ：？！1234567890 ，。？！；：、\r\t'  # 停用词
path = 'G:/学习/大三上/文本分析/test/'  # 文件路径


# 将txt文件分词保存，变量分别为文件路径，对应类别，编码格式，分词汇总文档文件流，类型汇总文档文件流
def txt_sum(txt_path, cla_tag, en_code, f1, f2, rate, id1, id2):
    index11,index22=id1,id2
    with open(txt_path, 'r', encoding=en_code) as jo:
        data = jo.read()
    data = re.sub(r'[{}]+'.format(punctuation), ' ', data)
    dataList = data.split('\n')
    count = 0
    print(len(dataList))
    for line in dataList:
        random.seed(time.time())
        rd = random.randint(1, rate)
        if rd == 1:
            if count == 0:
                count = count + 1
                file = f1
                index11 = index11 + 1
                index = index11
            else:
                count = count - 1
                file = f2
                index22 = index22 + 1
                index = index22
            file.write(str(index))
            file.write('\t')
            file.write(str(cla_tag))
            file.write('\t')
            file.write(line)
            file.write('\n')
    print(index22)
    print('success')
    return index11, index22


# 主程序
patha = path + 'train4.tsv'
pathb = path + 'test4.tsv'
f1 = open(patha, "a+", encoding='utf-8')
f2 = open(pathb, "a+", encoding='utf-8')
path1 = path + 'shi.txt'
index1 = 0
index2 = 0
index1, index2 = txt_sum(path1, 1, 'utf-8', f1, f2, 1, index1, index2)
path2 = path + 'ci.txt'
index1, index2 = txt_sum(path2, 2, 'utf-8', f1, f2, 1, index1, index2)
path3 = path + '文言文.txt'
index1, index2 = txt_sum(path3, 3, 'utf-8', f1, f2, 1, index1, index2)
path4 = path + '新闻.txt'
index1, index2 = txt_sum(path4, 4, 'gbk', f1, f2, 80, index1, index2)
path5 = path + '期刊论文.txt'
index1, index2 = txt_sum(path5, 5, 'utf-8', f1, f2, 80, index1, index2)
print(index1, index2)
f1.close()
f2.close()
