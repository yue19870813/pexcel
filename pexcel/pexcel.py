#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: pexcel.py

import sys, getopt, config, language
from interpreter import interpreter

__author__ = 'ituuz'

"""
这个是整个程序的入口文件，负责初始化一些东西，激活一些配置，调用后续功能。
"""

print("The author is " + config.__author__)

# 当前版本号
VERSION = "v0.0.1"

# 入口函数
def main(argv):
	# 测试接口
	# interpreter.runByPath("E:/pexcel.git/trunk/pexcel");

	# 获取命令行参数，如果没有命令行参数则根据config.py配置进行生成
	try:
		# 获取命令行参数
		opts, args = getopt.getopt(argv,"i:o:f:g:t:e:l:p:vh")
	except getopt.GetoptError:
		print(language.COMMAND_ERROR_TIPS)
		print(language.HELP_CONTENT)

	# 取得所有命令行参数
	command_i = "" # excel源文件目录
	command_o = "" # 生成文件输出目录
	command_f = "" # 文件列表
	command_g = "" # 文件分组列表
	command_t = "" # 最终生成的数据类型
	command_e = "" # 数据加密类型
	command_l = "" # 生成的工具类库类型
	command_p = "" # 生成的数据文件后缀名

	for opt, arg in opts:
		print(opt + "  " + arg)
		if opt == '-i':
			command_i = arg
		elif opt == '-o':
			command_o = arg
		elif opt == '-f':
			command_f = arg
		elif opt == '-g':
			command_g = arg
		elif opt == '-t':
			command_t = arg
		elif opt == '-e':
			command_e = arg
		elif opt == '-l':
			command_l = arg
		elif opt == '-p':
			command_p = arg
		elif opt == '-v':
			print("v0.0.1")
			sys.exit()
		elif opt == '-h' or opt == "help":
			print(language.HELP_CONTENT)
			sys.exit()
		else:
			print ("命令行参数使用错误：" + opt + "  " + arg)
			sys.exit()


	# 开始处理命令行参数逻辑
	if command_o == "":
		# 命令行输出为空则读取config中的配置
		command_o = config.OUTPUT_PATH
		# 如果还为空则终止程序
		if command_o == "":
			print("数据文件输出目录不能为空!")
			sys.exit()


	# 判断输入目录是否为空
	if command_i == "" and command_f == "" and command_g == "":
		# 如果为空则使用config中的配置
		command_i = config.INPUT_PATH
		# 如果还为空则终止程序
		if command_i == "":
			print("输入目录不能为空!")
			sys.exit()

	

	# 解析其他可选参数
	if command_t != "":
		# TODO:获取最终生成的数据类型
		pass
	if command_e != "":
		# TODO:数据加密类型
		pass
	if command_l != "":
		# TODO:生成的工具类库类型
		pass
	if command_p != "":
		# TODO:生成的数据文件后缀名
		pass

	# 根据上面对参数的解析调用不同配置和接口
	if command_i != "":
		# excel目录不为空，则为对整个目录生成数据
		interpreter.runByPath(command_i)
		pass
	elif command_f != "":
		# 对给的指定文件列表进行数据生成
		# TODO
		pass
	elif command_g != "":
		# 对分组进行数据生成
		# TODO
		pass



# 程序入口
if __name__ == "__main__":
	main(sys.argv[1:])
else:
	main();