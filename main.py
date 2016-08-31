#!usr/bin/env python
# -*- coding:utf-8 -*-
#main
from data_processing import *
from data_analysis import *
from product_result import *
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def main():
	splitTrainData()
	firstAnalysis()
	productResult()
	productResult_2()
	secondAnalysis()
	productResult_3()
	thirdAnalysis()
	productResult_4()
	fourthAnalysis()
	productResult_5()
	fifthAnalysis()
	productResult_6()
if __name__ == '__main__':
	main()