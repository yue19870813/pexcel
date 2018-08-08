#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: template.py

from mako.template import Template

' template module '

__author__ = 'ituuz'

mytemplate = Template(filename='./util/template/class.template')

top = ("// test1 \n\tpublic test1:number;", "// test2 \n\tpublic test2:string;")

print (mytemplate.render(name='TestVO', keyName='id', keyType='number', topics=top))

