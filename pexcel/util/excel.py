#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: excel.py
import openpyxl
import os

' excel module '

__author__ = 'ituuz'

"""
本模块是完全处理excel所需要的所有接口
Excel 格式如下：
配表名字	template
描述		配表测试模版	
其他		作者:ituuz  日期：2018-04-24	
id			数值		说明
int			string		string
int			string	
id			value		des
KEY		
10000		test1		测试1
21001		test2		测试2
22001		test3		测试3

NOTE:
模版文件参考template目录下的t_template.xlsx文件
"""


"""
将excel转换为数据列表
filename: excel文件路径
return：表名，配表描述，配表其他信息，数据

数据格式：[
			[属性名1, 属性名2，属性名3],
			[数据类型1,数据类型2, 数据类型3],
			[数据1, 数据2, 数据3],
			...
			...
			...
			[数据1, 数据2, 数据3]
		  ]
"""

def convertExcel2List(filename, sheetname):
	data = openpyxl.load_workbook(filename)
	if(sheetname == ""):
		sheet = data.get_active_sheet()
	else:
		sheet = data.get_sheet_by_name(sheetname)

	excelName = sheet.cell(row=1, column=2).value
	excelDes = sheet.cell(row=2, column=2).value
	excelOther = sheet.cell(row=3, column=2).value

	print("表名：", excelName)
	print("配表描述：", excelDes)
	print("配表其他信息：", excelOther)

	print("属性名：", end="")
	for rowProperty in sheet.iter_rows(min_row=4, max_col=3, max_row=4):
		for cell in rowProperty:
			print(cell.value, "\t", end=",")
	print()

	print("数据类型：", end="")
	for rowNumClass in sheet.iter_rows(min_row=6, max_col=3, max_row=6):
		for cell in rowNumClass:
			print(cell.value, "\t", end=",")
	print()

	print("数据：")
	for row in sheet.iter_rows(min_row=9, max_col=3):
		for cell in row:
			print(cell.value, "\t", end=",")
		print()
	

def main():
	convertExcel2List("../../template/t_template.xlsx", "")

if __name__=="__main__":
	main()


