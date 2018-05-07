#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: language.py

import config

' language module '

__author__ = 'ituuz'

"""
这个是语言配置模块及多语言文本配置
"""

# 命令行帮助信息
HELP_CONTENT_ZH = """
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
	-l 生成的工具类库类型，可选类型有[ts|js|c|java|python]，默认不生成类库文件。 
	-p 生成的数据文件后缀名，默认为：ped。
	-v 工具当前版本号。
	-h 命令行帮助信息。
	其他有关信息请参考：https://github.com/yue19870813/pexcel/blob/master/README.md
---------------------------------------------
"""

HELP_CONTENT_EN = """
------------The command introduce--------------
method：
	对指定目录里excel进行生成：
	python pexcel.py -i xxx -o xxx 
  或：
	对所给的文件列表进行生成：
	python pexcel.py -f xxx,xxx,xxx -o xxx
  或：
	根据所给的分组文件数据进行生成
	python pexcel.py -g key1:xxx,xxx,xxx|key2:xxx,xxx -o xxx
important parameter：
	-i excel源文件目录
	-o 生成文件输出目录
	-f 文件列表 格式为：xxx,xxx,xxx
	-g 文件分组列表 格式为：xxx,xxx,xxx
option parameter：
	-t 最终生成的数据类型，可选类型有[json|bin|txt]，默认为json。 
	-e 数据加密类型[n|b|r]，b是Base64，r是RSA，n是不加密，默认为n。 
	-l 生成的工具类库类型，可选类型有[ts|js|c|java|python]，默认不生成类库文件。 
	-p 生成的数据文件后缀名，默认为：ped。
	-v 工具当前版本号。
	-h 命令行帮助信息。
	其他有关信息请参考：https://github.com/yue19870813/pexcel/blob/master/README.md
---------------------------------------------
"""

HELP_CONTENT = (HELP_CONTENT_ZH if (config.CURR_LANGUAGE == config.LanguageType.ZH) else HELP_CONTENT_EN)


# 命令行错误提示
COMMAND_ERROR_TIPS_ZH = "确定你的命令或参数是否正确，请参考帮助信息。"
COMMAND_ERROR_TIPS_EN = "Make sure your command is right，please refer to help information."
COMMAND_ERROR_TIPS = (COMMAND_ERROR_TIPS_ZH if (config.CURR_LANGUAGE == config.LanguageType.ZH) else COMMAND_ERROR_TIPS_EN)

# other....