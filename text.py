# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 11:35:10 2020

@author: MTAEXAM
"""
x = input()
a = []
b = {}
i = 1
r = 0
while i<1000001:
    while True:
    if x%i == 0:
        if i not in a:
            a.append(i)
        x = x/i
        r+=1
        
    else:
        i+=1
