#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: interpreter.py

import os
import os.path

from util import excel
from generator import generator

' interpreter module '

__author__ = 'ituuz'

"""
本模块是一个解释器的功能，主要功能就是负责获取原始数据。
"""

# 缓存所有数据，key-value，key为表名，value为数据。
tableDataDict = {}

# 存储表格数据的结构体
class DataStruct(object):
	"""
	该结构体用于存储单个表格的数据
	tableName: 表格名字
	tableDes: 表格描述
	tableElse: 表格其他信息
	tableData: 表格数据集合
	"""
	def __init__(self, tableName, tableDes, tableElse, columnDes, 
		columnType, columnName, talbeKey, tableData):
		super(DataStruct, self).__init__()
		self.tableName = tableName
		self.tableDes = tableDes
		self.tableElse = tableElse
		self.columnDes = columnDes
		self.columnType = columnType
		self.columnName = columnName
		self.talbeKey = talbeKey
		self.tableData = tableData

	def __str__(self):
		return "Table name:" + self.tableName + "\n\
Table des:" + self.tableDes + "\n\
Table else:" + self.tableElse



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
	# 生成目标数据格式
	generator.generate(tableDataDict)

def getData(path):
	# 获取path目录下所有文件
	fileList = os.listdir(path)  
	for filename in fileList:
		pathTemp = os.path.join(path,filename) 
		if os.path.isdir(pathTemp):
			getData(pathTemp)
		else:
			## 非excel文件不做处理
			if os.path.splitext(pathTemp)[1] != ".xlsx":
				continue
			## 处理数据
			print("生成该文件数据：" + pathTemp)
			excelData = excel.convertExcel2List(pathTemp, "")
			tableName = excelData[0]
			tableDes = excelData[1]
			tableElse = excelData[2]
			columnDes = excelData[3]
			columnType = excelData[4]
			columnName = excelData[5]
			tableKey = excelData[6]
			tableData = excelData[7]
			# 封装一个配表带数据结构
			dataObj = DataStruct(tableName, tableDes, tableElse, columnDes, 
				columnType, columnName, tableKey, tableData)
			tableDataDict[tableName] = dataObj

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