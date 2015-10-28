# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 12:35:33 2015

@author: jakobunfried
"""

for i in range(1,101):
    text = ""
    if i%3 == 0:
        text = text + "bizz "
    if i%5 == 0:
        text = text + "buzz "
    if i%7 == 0:
        text = text + "woof "
    if len(text) == 0:
        text = i
    print "[%d] %s" % (i,text)