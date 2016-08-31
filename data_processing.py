#!usr/bin/env python
# -*- coding:utf-8 -*-
#训练数据处理
import json
import re
import string
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

#获取训练数据中的文本，及Json输出结果，生成训练数据
def splitTrainData():
	inFile=open('data/opendata.txt','r')
	trainDataFile=open('data/trainData.dat','w')
	delset = string.punctuation #英文标点
	for line in inFile.readlines():
		line=line.strip().replace('\b','')
		content=line.split('\t')
		core_entity=json.loads(content[1])[0]["core_entity"]
		content=content[0]
		#清理部分字符
		content=content.replace("(","（").replace(")","）").replace(" ","")
		content=content.replace(",",'，').replace(".",'。')
		content=content.translate(None,delset)#英文标点去除
		content=re.compile(r'\d*\w*').sub("",content)#去除英文及数字
		content=re.compile(r'（.*）').sub("",content)#去除（）及里面内容
		if core_entity==[]:
			continue
		if content.find(core_entity[0])==-1:
			continue
		trainDataFile.write("︽︽%s︽,%s\n" % (content,core_entity[0]))
	trainDataFile.close()
	inFile.close()
