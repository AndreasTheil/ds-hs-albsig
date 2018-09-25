# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 22:29:49 2018

@author: Sergej Schweizer (sergej.schweizer@gmail.com)
"""




"""
Suggested solution for the "Kontrolaufgabe 1.7"
"""

def myEnumerate(mylist):
    return [ x for x in map(lambda x,y: (x,y), range(0,len(mylist)), mylist) ]

print(myEnumerate("bla"))
