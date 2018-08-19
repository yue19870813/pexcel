#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: config.py
from enum import Enum

' config module '

__author__ = 'ituuz'

"""
此文件是用于保存全局设置的，包括命令行传入的参数以及后期GUI上用户选择的参数等。
同时里面的设置可以手动填写，命令行参数会覆盖手动填写的参数。
"""
# 是否是调试模式
IS_DEBUG = True

# 最终生成数据类型枚举
OutputDataType = Enum('OutputDataType', ('Json', 'Binary', 'Text'))

# 最终生成数据的加密类型枚举
DataEncryptType = Enum('DataEncryptType', ('NoEncrypt', 'Base64', 'RSA'))

# 系统语言枚举
LanguageType = Enum('LanguageType', ('EN', 'ZH'))

"""
以下为详细配置，可手动配置，可用命令行或者GUI参数覆盖。
"""
# 生成的工具类库类型枚举
LibsType = Enum('LibsType', ('TypeScript', 'JavaScript', 'C', 'Java', 'Python'))

# 目标excel文件路径 
INPUT_PATH = "./../template/"

# 最终输出目录
OUTPUT_PATH = "./../output/"

# 生成的数据类型
OUTPUT_DATA_TYPE = OutputDataType.Text

# 生成数据的加密方式
DATA_ENCRYPT_TYPE = DataEncryptType.NoEncrypt

# 生成文件后缀名
OUTPUT_FILE_POSTFIX = "ped"

# 生成的配套工具类库类型
OUTPUT_LIBS_TYPE = LibsType.TypeScript

# 当前语言
CURR_LANGUAGE = LanguageType.ZH
