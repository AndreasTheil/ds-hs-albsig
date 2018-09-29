# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 22:03:02 2018

@author: Sergej Schweizer 
@mail:   sergej.schweizer@gmail.com

"""

 [ lines.split()[0] 
     for lines in f.splitlines() 
         if len(lines) > 0 
 ]
 
 [ lines for lines in f.splitlines() 
     if len(lines) > 0 and lines[0].islower() 
 ]
 
 max(
     [ len(
        [ word for word in words.split() if word.islower() ]
        )  
           for words in f.splitlines() ] 
     )