# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 19:43:02 2018

@author: Sergej Schweizer 
@mail:   sergej.schweizer@gmail.com

"""

from os import listdir

# 1.28a
 [  (len(fil),fil ) for fil in listdir('.') ]
 
 #1.28b
 [  fil  for fil in listdir('.') if fil.split('.')[-1]=='js' ]
 
 #1.28c
 
 max(
    list(
        map(
            lambda x: (len(open(x).read().split()),x), 
            [ fil  for fil in listdir('.') if fil.split('.')[-1]=='js' ]
            )
        )
    )
        

# 1.28d
max(
    list(
        map(
            lambda x: (x,len(list(filter(
                lambda y: y if len(y)>10 else False,
                open(x).read().split()
                )))),
            [ fil  for fil in listdir('.') if fil.split('.')[-1]=='js' ]
            )
        )
    )[0]