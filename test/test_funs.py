# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 10:57:14 2019

@author: Radek
"""
import sys

sys.path.insert(1, 'D:/Dokumenty/Studia/Master2/DevOps/PytestProject')
import funs

def test_add():
    assert funs.add(1,2) == 3


