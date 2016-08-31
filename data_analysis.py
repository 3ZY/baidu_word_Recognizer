#!usr/bin/env python
# -*- coding:utf-8 -*-
#统计分析数据
from __future__ import division
import operator
import string
import re
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def firstAnalysis():
	inFile=open('data/trainData.dat','r')
	for i in xrange(1,3):
		tag_true_num={}
		tag_rate={}
		inFile.seek(0)	
		for line in inFile.readlines():
			line=line.strip()
			content,core_entity=line.split(',')
			pre_c,next_c=content.split(core_entity)[:2]
			key="%s,%s" % (pre_c[-(3*i):],next_c[:(3*i)])
			tag_true_num.setdefault(key,0)
			tag_true_num[key]+=1
		
		for key,value in tag_true_num.items():
			count=10
			pre_c,next_c=key.split(',')
			p=re.compile( r'a[^ab]+b')
			inFile.seek(0)
			for line in inFile.readlines():
				line=line.replace(pre_c,"a").replace(next_c,"b")
				for tmp in p.findall(line):
					if tmp[1:-1].find("，")==-1 and tmp[1:-1].find("︽")==-1:
						count+=1
			tag_rate[key]=[value,count,value/count]
			
		tagFile=open('data/tag_rate_%d.dat' % i,'w')
		tagGoalFile=open('data/tag_goal_%d.dat' % i,'w')
		tagGoalFile.write('pre,next\n')
		tagFile.write('pre,next,true_num,all_num,rate\n')
		for key,values in sorted(tag_rate.items(),key=lambda x:x[1][2],reverse=True):
			if values[0]<1 or values[0]>values[1]-1 or values[1]==10: 
				continue
			tagFile.write("%s,%d,%d,%f\n" % (str(key),values[0],values[1],values[2]))
		 	tagGoalFile.write("%s\n" % str(key) )
		tagGoalFile.close()
		tagFile.close()
	inFile.close()

def secondAnalysis():
	#停用词
	stopFile=open('data/stopWord.txt','r')	
	stopWords=[]
	for line in stopFile.readlines():
		line=line.strip()
		if int(len(line)/3)!=len(line)/3 or len(line)<3:
			continue
		stopWords.append(line)
	stopFile.close()
	
	#情感词
	emotionFile=open('data/emotion.txt','r')
	emotionWords=[]
	for line in emotionFile.readlines():
		emotionWords.append(line.strip())
	emotionFile.close()

	keywords=[]
	goalFile=open('data/trainData_3.dat','r')
	for line in goalFile.readlines():
		content=line.strip()[6:]		
		core_entity=content.split("︽,")[1]
		#content=content.split("︽,")[0]
		if len(core_entity)<=3:
			continue
		flag=True
		for stopWord in stopWords:
			if core_entity.find(stopWord)!=-1:
				flag=False
				break
		if core_entity in emotionWords:
			continue
		if flag and core_entity not in keywords:
			keywords.append(core_entity)

	#按长度决定优先级
	keywords=sorted(keywords,key=lambda x:len(x),reverse=True)

	keywordFile=open('data/keyword.dat','w')
	for keyword in keywords:
		if len(keyword)<=6 or keyword.find('年')!=-1:
			continue
		keyword=keyword.replace("“","").replace("”","")
		keywordFile.write(keyword+'\n')
	keywordFile.close()

def thirdAnalysis():
	keyword_num={}
	goalFile=open('data/trainData_4.dat','r')
	for line in goalFile.readlines():
		content=line.strip()[6:]
		core_entity=content.split("︽,")[1]
		keyword_num.setdefault(core_entity,0)
		keyword_num[core_entity]+=1

	keywordFile=open('data/keyword_num.dat','w')
	for keyword,num in sorted(keyword_num.items(),key=operator.itemgetter(1),reverse=True):
		keyword=keyword.replace("“","").replace("”","")
		keywordFile.write(keyword+","+str(num)+'\n')
	keywordFile.close()

	#停用词
	stopFile=open('data/stopWord.txt','r')	
	stopWords=[]
	for line in stopFile.readlines():
		line=line.strip()
		if int(len(line)/3)!=len(line)/3 or len(line)<3:
			continue
		stopWords.append(line)
	stopFile.close()
	
	#情感词
	emotionFile=open('data/emotion.txt','r')
	emotionWords=[]
	for line in emotionFile.readlines():
		emotionWords.append(line.strip())
	emotionFile.close()

	errorFile=open('data/error_word.dat','w')
	for keyword in keyword_num.keys():
		if len(keyword)<=3:
			errorFile.write(keyword+'\n')
			continue
		if keyword.find('年')!=-1 and keyword.find('月')!=-1:
			errorFile.write(keyword+'\n')
			continue
		if keyword in emotionWords:
			errorFile.write(keyword+'\n')
			continue
		for stopWord in stopWords:
			if keyword.find(stopWord)!=-1:
				errorFile.write(keyword+'\n')
				break
	errorFile.close()

def fourthAnalysis():
	keyword_num={}
	goalFile=open('data/trainData_5.dat','r')
	for line in goalFile.readlines():
		content=line.strip()[6:]		
		core_entity=content.split("︽,")[1]
		#content=content.split("︽,")[0]
		keyword_num.setdefault(core_entity,0)
		keyword_num[core_entity]+=1

	keywordFile=open('data/keyword_num.dat','w')
	for keyword,num in sorted(keyword_num.items(),key=operator.itemgetter(1),reverse=True):
		keyword=keyword.replace("“","").replace("”","")
		keywordFile.write(keyword+","+str(num)+'\n')
	keywordFile.close()

	#停用词
	stopFile=open('data/stopWord.txt','r')	
	stopWords=[]
	for line in stopFile.readlines():
		line=line.strip()
		if int(len(line)/3)!=len(line)/3 or len(line)<3:
			continue
		stopWords.append(line)
	stopFile.close()
	
	#情感词
	emotionFile=open('data/emotion.txt','r')
	emotionWords=[]
	for line in emotionFile.readlines():
		emotionWords.append(line.strip())
	emotionFile.close()

	errorFile=open('data/error_word.dat','w')
	for keyword in keyword_num.keys():
		if len(keyword)<=3:
			errorFile.write(keyword+'\n')
			continue
		if keyword.find('年')!=-1 and keyword.find('月')!=-1:
			errorFile.write(keyword+'\n')
			continue
		if keyword in emotionWords:
			errorFile.write(keyword+'\n')
			continue
		for stopWord in stopWords:
			if keyword.find(stopWord)!=-1:
				errorFile.write(keyword+'\n')
				break
	errorFile.close()

def fifthAnalysis():
	keyword_num={}
	goalFile=open('data/trainData_6.dat','r')
	for line in goalFile.readlines():
		content=line.strip()[6:]		
		core_entity=content.split("︽,")[1]
		#content=content.split("︽,")[0]
		keyword_num.setdefault(core_entity,0)
		keyword_num[core_entity]+=1

	keywordFile=open('data/keyword_num.dat','w')
	for keyword,num in sorted(keyword_num.items(),key=operator.itemgetter(1),reverse=True):
		keyword=keyword.replace("“","").replace("”","")
		keywordFile.write(keyword+","+str(num)+'\n')
	keywordFile.close()

	#停用词
	stopFile=open('data/stopWord.txt','r')	
	stopWords=[]
	for line in stopFile.readlines():
		line=line.strip()
		if int(len(line)/3)!=len(line)/3 or len(line)<3:
			continue
		stopWords.append(line)
	stopFile.close()
	
	#情感词
	emotionFile=open('data/emotion.txt','r')
	emotionWords=[]
	for line in emotionFile.readlines():
		emotionWords.append(line.strip())
	emotionFile.close()

	errorFile=open('data/error_word.dat','w')
	for keyword in keyword_num.keys():
		if re.match(r'[a-zA-Z]',keyword):
			continue
		count=0
		if len(keyword)<=3:
			errorFile.write(keyword+'\n')
			continue
		if keyword.find('年')!=-1 and keyword.find('月')!=-1:
			errorFile.write(keyword+'\n')
			continue
		if keyword in emotionWords:	
			errorFile.write(keyword+'\n')
			continue
		for stopWord in stopWords:
			if keyword.find(stopWord)!=-1:
				count+=len(stopWord)
		if count/len(keyword)>0.5:
			errorFile.write(keyword+'\n')
	errorFile.close()