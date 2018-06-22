#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: generator.py

import json
import config, language
from util import excel
# from interpreter import interpreter

' generator module '

__author__ = 'ituuz'

"""
本模块是一个生成器的功能，主要功能就是负责将原始数据生成指定文件。
"""

"""
将配表的数据集合生成指定文件
"""
def generate (tableDataDict):
	if config.OUTPUT_DATA_TYPE == config.OutputDataType.Json:
		jsonStr = toJson(tableDataDict)
	elif config.OUTPUT_DATA_TYPE == config.OutputDataType.Text:
		textStr = toText(tableDataDict)
	elif config.OUTPUT_DATA_TYPE == config.OutputDataType.Binary:
		toBinary(tableDataDict)
	else:
		# 不存在这种生成数据的格式
		print (language.DATA_GENERATE_TYPE_NOT_EXIST + "：" + config.OUTPUT_DATA_TYPE)


# 将数据转换为json格式字符串
def toJson(tableDataDict):
	"""
	{
		"tName": "nnn",
		"tDes": "xxx",
		"tOther": "xxx",
		"cDes": ["序号", "xx", "xx"],
		"cType": ["int", "string", "string"],
		"cName": ["id", "xx", "yy"],
		"tKey": [1, 1, 0],
		"tData": [{
				"id": 10000,
				"xx": "10001_200,10002_1,10004_5",
				"yy": "AAA"
			},
			{
				"id": 21001,
				"xx": "10004_1000,10001_1000",
				"yy": "BBB"
			},
			{
				"id": 22001,
				"xx": "10004_1000",
				"yy": "CCC"
			}
		]
	}
	"""
	# listExcel = excel.convertExcel2List("../template/t_template.xlsx", "")
	for k, v in tableDataDict.items():
		print ("-------------------------")
		print (k)
		print (v)
		print (v.tableData)
		print ("*************************")
		print (json.dumps(v.tableData))

	return "json"

# 将数据转换成纯文本格式数据
def toText(tableDataDict):
	"""
	int,string,string
	id,xx,yy
	10000,10001_200,10002_1
	10001,10004_1000,BBB
	10002,10003_444,ccc
	"""
	return "text"

# 将数据转换为二进制格式数据
def toBinary(tableDataDict):
	pass


def main():
	toJson()

if __name__ == "__main__":
	main()