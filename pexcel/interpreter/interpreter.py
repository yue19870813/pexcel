#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: excel.py

import os
import os.path

' excel interpreter '

__author__ = 'ituuz 111'

"""
本模块是一个解释器的功能，主要功能就是负责获取原始数据。
"""

# 存储表格数据的结构体
class DataStruct(object):
	"""
	该结构体用于存储单个表格的数据
	tableName: 表格名字
	tableDes: 表格描述
	tableElse: 表格其他信息
	tableData: 表格数据集合
	"""
	def __init__(self, tableName, tableDes, tableElse, tableData):
		super(ClassName, self).__init__()
		self.tableName = tableName
		self.tableDes = tableDes
		self.tableElse = tableElse
		self.tableData = tableData
	
	# 将数据转换为json格式字符串
	def toJson(self):
		pass		

	# 将数据转换成纯文本格式数据
	def toText(self):
		pass

	# 将数据转换为二进制格式数据
	def toBinary(self):
		pass

		

"""
这里根据配置生成指定的各类数据并控制整体流程
遍历指定路径文件进行生成
"""
def runByPath(path):
	if not os.path.isdir(path):
		print(path + "不是一个路径，请检查你的配置路径。")
		return
	# 递归遍历目录解析excel文件
	getData(path)

def getData(path):
	#获取path目录下所有文件
	fileList = os.listdir(path)  
	for filename in fileList:
		pathTemp = os.path.join(path,filename) 
		if os.path.isdir(pathTemp):
			getData(pathTemp)
		else:
			## TODO:处理数据
			print("生成该文件数据：" + pathTemp)
			pass

"""
根据传入的文件列表进行生成
"""
def runByList(list):
	pass


"""
根据传入的文件分组进行生成
"""
def runByGroup(group):
	pass