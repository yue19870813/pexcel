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
		toJson(tableDataDict)
	elif config.OUTPUT_DATA_TYPE == config.OutputDataType.Text:
		pass
	elif config.OUTPUT_DATA_TYPE == config.OutputDataType.Binary:
		pass
	else:
		# 不存在这种生成数据的格式
		print (language.DATA_GENERATE_TYPE_NOT_EXIST + "：" + config.OUTPUT_DATA_TYPE)


# 将数据转换为json格式字符串
def toJson(tableDataDict):
	"""
	[
		tName:"nnn",
		tDes:"xxx",
		tOther:"xxx",
		tKey:[1,1,0],
		tData:[
			[10000, "10001_200,10002_1,10004_5", "AAA"], 
			[21001, "10004_1000,10001_1000", "BBB"], 
			[22001, "10004_1000", "CCC"]
		]
	]


	"""
	# listExcel = excel.convertExcel2List("../template/t_template.xlsx", "")
	for k, v in tableDataDict.items():
		print ("-------------------------")
		print (k)
		print (v)
		print (v.tableData)
		print ("*************************")
		print (json.dumps(v.tableData))

		

# 将数据转换成纯文本格式数据
def toText(self):
	pass

# 将数据转换为二进制格式数据
def toBinary(self):
	pass


def main():
	toJson()

if __name__ == "__main__":
	main()