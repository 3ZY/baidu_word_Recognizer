随心所写，代码较乱

第二届百度&amp;西安交通大学大数据竞赛

环境：python2.7

	外部库：json（不重新训练则不需要）
	
（python2 + json 对编码要求还是比较严格的，至少读训练集没报错，便没特殊处理了）

	data目录：
	
		emotion.txt  -> 外部情感词汇库
		
		stopWord.txt  -> 外部停用词汇库
		
		opendata.txt  ->  训练数据文件名 （替换数据请改成此文件名）
		
		opendata_20w  ->  测试数据文件名 （替换数据请改成此文件名）
		
		result.txt  ->  生成的结果文件
		
		tag_goal_#  ->  从训练数据中提取的标签
		
		tag_rate_#  ->  从训练数据中提取的标签
		
		其他  ->  中间过程数据
		
	运行main.py文件即可：
	
		splitTrainData(), firstAnalysis() 为训练生成标签，其余均生成结果，及对结果优化
		

解题思路：

http://blog.csdn.net/three_fish/article/details/52382610
