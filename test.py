#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 14:13:04 2022

@author: dineshchhantyal
"""


x = str(-24436)
rev = 0
n=1
while n!= len(x)+1:
    rev = rev * 10 + int(x[len(x)-n])
    n+=1

print(rev)
    