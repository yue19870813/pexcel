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
	