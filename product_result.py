#!usr/bin/env python
# -*- coding:utf-8 -*-
#生成结果
import re
import string
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def productResult():
	
	tagGoalFile=open('data/tag_goal_2.dat','r')
	tags=[]
	tagGoalFile.readline()
	for line in tagGoalFile.readlines():
		tags.append(line.strip())

	goalFile=open('data/opendata_20w','r')
	resultAlFile=open('data/trainData_2.dat','w')
	result={}
	p=re.compile( r',[^,!]+!')
	delset = string.punctuation #英文标点
	for line in goalFile.readlines():
		content=line.strip()
		result["content"]=content
		content=content.replace("(","（").replace(")","）").replace(" ","")
		content=content.replace(",",'，').replace(".",'。')
		content=content.translate(None,delset)#英文标点去除
		content=content.replace("综述：","")
		content=content.replace("优点：","")
		content=content.replace("缺点：","")
		content=re.compile(r'（.*）').sub("",content)#去除（）及里面内容
		content="︽︽%s︽" % content
		
		flag=False
		for tag in tags:
			pre_c,next_c=tag.split(',')
			da_content=content.replace(pre_c,",").replace(next_c,"!")
			for tmp in p.findall(da_content):
				if tmp[1:-1].find("，")==-1 and tmp[1:-1].find("︽")==-1:
					result["core_entity"]=tmp[1:-1]
					flag=True
					break
			if flag:
				break
		if flag:
			resultAlFile.write("︽︽%s︽,%s\n" % (result["content"],result["core_entity"]) )

	resultAlFile.close()
	goalFile.close()
	tagGoalFile.close()

def productResult_2():

	tagGoalFile=open('data/tag_goal_2.dat','r')
	tags=[]
	tagGoalFile.readline()
	for line in tagGoalFile.readlines():
		tags.append(line.strip())

	goalFile=open('data/trainData_2.dat','r')
	resultAlFile=open('data/trainData_3.dat','w')
	result={}
	p=re.compile( r',[^,!]+!')
	delset = string.punctuation #英文标点
	for line in goalFile.readlines():
		content=line.strip()[6:]
		result["content"]=content.split("︽,")[0]
		result["core_entity"]=content.split("︽,")[1]
		content=content.split("︽,")[1]
		content=content.translate(None,delset)#英文标点去除
		content="︽︽%s。︽" % content
		
		if result["content"].find("《")==-1:
			flag=False
			for tag in tags:
				pre_c,next_c=tag.split(',')
				da_content=content.replace(pre_c,",").replace(next_c,"!")
				for tmp in p.findall(da_content):
					if tmp[1:-1].find("，")==-1 and tmp[1:-1].find("︽")==-1:
						result["core_entity"]=tmp[1:-1]
						flag=True
						break
				if flag:
					break

		resultAlFile.write("︽︽%s︽,%s\n" % (result["content"],result["core_entity"]) )

	resultAlFile.close()
	goalFile.close()
	tagGoalFile.close()

def productResult_3():

	keywords=[]
	keywordFile=open('data/keyword.dat','r')
	for line in keywordFile.readlines():
		keywords.append(line.strip())
	keywordFile.close()

	goalFile=open('data/trainData_3.dat','r')
	resultAlFile=open('data/trainData_4.dat','w')
	result={}
	delset = string.punctuation #英文标点
	for line in goalFile.readlines():
		content=line.strip()[6:]
		result["content"]=content.split("︽,")[0]
		result["core_entity"]=content.split("︽,")[1]
		content=content.split("︽,")[1]
		content=content.translate(None,delset)#英文标点去除
		
		if result["content"].find("《")==-1:
			for keyword in keywords:
				if content.find(keyword)!=-1:
					result["core_entity"]=keyword
					break
		resultAlFile.write("︽︽%s︽,%s\n" % (result["content"],result["core_entity"]) )

	resultAlFile.close()
	goalFile.close()

def productResult_4():
	tagGoalFile=open('data/tag_goal_1.dat','r')
	tags=[]
	tagGoalFile.readline()
	for line in tagGoalFile.readlines():
		tags.append(line.strip())

	error_words=[]
	erroFile=open('data/error_word.dat','r')
	for line in erroFile.readlines():
		error_words.append(line.strip())
	erroFile.close()


	goalFile=open('data/trainData_4.dat','r')
	resultAlFile=open('data/trainData_5.dat','w')
	result={}
	p=re.compile( r',[^,!]+!')
	delset = string.punctuation #英文标点
	for line in goalFile.readlines():
		content=line.strip()[6:]
		result["content"]=content.split("︽,")[0]
		result["core_entity"]=content.split("︽,")[1]
		content=content.split("︽,")[1]
		content=content.translate(None,delset)#英文标点去除
		content="︽︽%s。︽" % content
		
		if result["content"].find("《")==-1:
			if result["core_entity"] in error_words:
				flag=False
				for tag in tags:
					pre_c,next_c=tag.split(',')
					da_content=content.replace(pre_c,",").replace(next_c,"!")
					for tmp in p.findall(da_content):
						if tmp[1:-1].find("，")==-1 and tmp[1:-1].find("︽")==-1:
							result["core_entity"]=tmp[1:-1]
							flag=True
							break
					if flag:
						break
	
		resultAlFile.write("︽︽%s︽,%s\n" % (result["content"],result["core_entity"]) )

	resultAlFile.close()
	goalFile.close()
	tagGoalFile.close()

def productResult_5():
	tagGoalFile=open('data/tag_goal_1.dat','r')
	tags=[]
	tagGoalFile.readline()
	for line in tagGoalFile.readlines():
		tags.append(line.strip())

	error_words=[]
	erroFile=open('data/error_word.dat','r')
	for line in erroFile.readlines():
		error_words.append(line.strip())
	erroFile.close()

	goalFile=open('data/trainData_5.dat','r')
	#resultFile=open('data/result.txt','w')
	resultAlFile=open('data/trainData_6.dat','w')
	result={}
	p=re.compile( r',[^,!]+!')
	delset = string.punctuation #英文标点
	for line in goalFile.readlines():
		content=line.strip()[6:]
		result["content"]=content.split("︽,")[0]
		result["core_entity"]=content.split("︽,")[1]
		content=content.split("︽,")[1]
		content=content.translate(None,delset)#英文标点去除
		content="︽︽%s。︽" % content
		
		if result["content"].find("《")==-1 or result["core_entity"].find("《")!=-1:
			if result["core_entity"] in error_words:
				flag=False
				for tag in tags:
					pre_c,next_c=tag.split(',')
					da_content=content.replace(pre_c,",").replace(next_c,"!")
					for tmp in p.findall(da_content):
						if tmp[1:-1].find("，")==-1 and tmp[1:-1].find("︽")==-1:
							result["core_entity"]=tmp[1:-1]
							flag=True
							break
					if flag:
						break
	
		#result_string="[{\"content\": \"%s\", \"core_entity\": [\"%s\"]}]\n" \
		#				% (result["content"],result["core_entity"])
		#resultFile.write(result_string)
		resultAlFile.write("︽︽%s︽,%s\n" % (result["content"],result["core_entity"]) )

	resultAlFile.close()
	goalFile.close()
	tagGoalFile.close()

def productResult_6():
	tagGoalFile=open('data/tag_goal_1.dat','r')
	tags=[]
	tagGoalFile.readline()
	for line in tagGoalFile.readlines():
		tags.append(line.strip())

	error_words=[]
	erroFile=open('data/error_word.dat','r')
	for line in erroFile.readlines():
		error_words.append(line.strip())
	erroFile.close()

	goalFile=open('data/trainData_6.dat','r')
	resultFile=open('data/result.txt','w')
	resultAlFile=open('data/trainData_7.dat','w')
	result={}
	p=re.compile( r',[^,!]+!')
	delset = string.punctuation #英文标点
	for line in goalFile.readlines():
		content=line.strip()[6:]
		result["content"]=content.split("︽,")[0]
		result["core_entity"]=content.split("︽,")[1]
		content=content.split("︽,")[0]
		content=content.replace("(","（").replace(")","）").replace(" ","")
		content=content.replace(",",'，').replace(".",'。')
		content=content.translate(None,delset)#英文标点去除
		content=re.compile(r'（.*）').sub("",content)#去除（）及里面内容
		content="︽︽%s︽" % content
		
		if result["core_entity"] in error_words:
			flag=False
			for tag in tags:
				pre_c,next_c=tag.split(',')
				da_content=content.replace(pre_c,",").replace(next_c,"!")
				for tmp in p.findall(da_content):
					if tmp[1:-1].find("，")==-1 and tmp[1:-1].find("︽")==-1:
						result["core_entity"]=tmp[1:-1]
						flag=True
						break
				if flag:
					break
		result["core_entity"]=result["core_entity"].replace("，",",").replace("。",".")

		result_string="[{\"content\": \"%s\", \"core_entity\": [\"%s\"]}]\n" \
						% (result["content"],result["core_entity"])
		resultFile.write(result_string)
		resultAlFile.write("︽︽%s︽,%s\n" % (result["content"],result["core_entity"]) )

	resultFile.close()
	goalFile.close()
	tagGoalFile.close()
