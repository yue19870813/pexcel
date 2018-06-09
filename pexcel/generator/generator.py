#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: generator.py

import config, language
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
		pass
	elif config.OUTPUT_DATA_TYPE == config.OutputDataType.Text:
		pass
	elif config.OUTPUT_DATA_TYPE == config.OutputDataType.Binary:
		pass
	else:
		# 不存在这种生成数据的格式
		print (language.DATA_GENERATE_TYPE_NOT_EXIST + "：" + config.OUTPUT_DATA_TYPE)


# 将数据转换为json格式字符串
def toJson(self):
	pass		

# 将数据转换成纯文本格式数据
def toText(self):
	pass

# 将数据转换为二进制格式数据
def toBinary(self):
	pass