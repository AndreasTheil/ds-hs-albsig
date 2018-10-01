# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 20:19:07 2018

@author: Sergej Schweizer 
@mail:   sergej.schweizer@gmail.com

"""

from os import walk

# 1.29a
list(max([[ (file, len(file)) for file in  files ] for cur,dirs,files in walk('.') ]))

# 1.29b
list(max([[ (file, file.count('e')) for file in  files ] for cur,dirs,files in walk('.') ]))