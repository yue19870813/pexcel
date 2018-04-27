#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: pexcel.py

import sys, getopt, config
from interpreter import interpreter

__author__ = 'ituuz'

"""
这个是整个程序的入口文件，负责初始化一些东西，激活一些配置，调用后续功能。
"""

print ("Hello world!")

print("The author is " + config.__author__)


# 命令行规则及使用介绍，HELE_CONTENT同时也用于帮助功能。
HELE_CONTENT = """
------------命令行参数使用介绍--------------
用法：
	对指定目录里excel进行生成：
	python pexcel.py -i xxx -o xxx 
  或：
	对所给的文件列表进行生成：
	python pexcel.py -f xxx,xxx,xxx -o xxx
  或：
	根据所给的分组文件数据进行生成
	python pexcel.py -g key1:xxx,xxx,xxx|key2:xxx,xxx -o xxx
重要参数：
	-i excel源文件目录
	-o 生成文件输出目录
	-f 文件列表 格式为：xxx,xxx,xxx
	-g 文件分组列表 格式为：xxx,xxx,xxx
可选参数：
	-t 最终生成的数据类型，可选类型有[json|bin|txt]，默认为json。 
	-e 数据加密类型[n|b|r]，b是Base64，r是RSA，n是不加密，默认为n。 
	-l 生成的工具类库类型，可选类型有[ts|js|c|java|python]，默认不生成类库。 
	-p 生成的数据文件后缀名，默认为：ped。
	-v 工具当前版本号。
	-h 命令行帮助信息。
	其他有关信息请参考：https://github.com/yue19870813/pexcel/blob/master/README.md
---------------------------------------------
"""


def main(argv):
	# 测试接口
	# interpreter.runByPath("E:/pexcel.git/trunk/pexcel");

	# TODO:获取命令行参数，如果没有命令行参数则根据config.py配置进行生成
	# 获取命令行参数
	opts, args = getopt.getopt(argv,"i:o:f:g:t:e:l:p:vh")


	print(argv)
	# 取得所有命令行参数

	command_i = "" # excel源文件目录
	command_o = "" # 生成文件输出目录
	command_f = "" # 文件列表
	command_g = "" # 文件分组列表
	command_t = "" # 最终生成的数据类型
	commond_e = "" # 数据加密类型
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
			print(HELE_CONTENT)
			sys.exit()
		else:
			print ("命令行参数使用错误：" + opt + "  " + arg)
			sys.exit()



if __name__ == "__main__":
	main(sys.argv[1:])