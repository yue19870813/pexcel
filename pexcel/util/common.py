#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: common.py
import config

' common module '

__author__ = 'ituuz'

"""
本模块是通用的公共接口等
"""

"""
日志打印接口：
方便打印调试，在非debug下不会打印
"""
def log(content):
	if config.IS_DEBUG:
		print("pexcel:" + content)
	

"""
用于打印错误提示等非调试的情况下也要显示的信息
后期在GUI中这些信息会以弹窗的形式展现
"""
def alert(content):
	print(content)