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

# 最终生成数据类型枚举
OutputDataType = Enum('OutputDataType', ('Json', 'Binary', 'Text'))

# 最终生成数据的加密类型枚举
DataEncryptType = Enum('DataEncryptType', ('None', 'Base64', 'RSA'))


"""
以下为详细配置，可手动配置，可用命令行或者GUI参数覆盖。
"""

# 生成的工具类库类型枚举
LibsType = Enum('LibsType', ('TypeScript', 'JavaScript', 'C', 'Java', 'Python'))

# 目标excel文件路径 
INPUT_PATH = "input path"

# 最终输出目录
OUTPUT_PATH = "output path"

# 生成的数据类型
OUTPUT_DATA_TYPE = OutputDataType.Json

# 生成数据的加密方式
DATA_ENCRYPT_TYPE = DataEncryptType.None

# 生成文件后缀名
OUTPUT_FILE_POSTFIX = "ped"

# 生成的配套工具类库类型
OUTPUT_LIBS_TYPE = LibsType.TypeScript
