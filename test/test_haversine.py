# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 10:57:14 2019

@author: Radek
"""

import sys

#################### MAKE CHANGES HERE #########################
sys.path.insert(1, 'D:/Dokumenty/Studia/Master2/DevOps/PytestProject') # path to testing file ("haversine.py")
########################### END ###############################

#import testing module
import haversine as hv


def test_putData():
    assert hv.putData() == True # functions already tested in test_datab.py
    
def test_getData():
    assert hv.getData() != None # functions already tested in test_datab.py
    