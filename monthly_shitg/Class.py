# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 11:56:10 2018

@author: Asako
"""

from enum import Enum


#define worker's inputs,condition and salary.
class Cnd(Enum):
    """
    Condition 
    W:The day, I Wanna work!!その日は出勤したい！
        cost rate == 0.5
    OK:The day,OK.問題なし！
        cost rate == 1.0
    P:The day, if Possible, I won't work..できれば休みたい
        cost rate == 1.5
    IM:The day,IMpossible to work!!働けない！
        cost rate ==inf
    """
    W = 0.5
    OK = 1
    P = 1.5
    IM = 1000000

class Slr(Enum):
    """
    Salary
    TR Trainer
        trainer who trains trainee
    TRE Trainee
        trainee who trained by trainer
    SY0 Service year 0
        worker who have worked for less than a year
    SY1 Service year 1
        worker who have worked for more than a year
    SY2 Service year 2
        worker who have worked for more than 2 years
    EX Experienced
        worker who experienced for more than 3 years
    MN Manager
        manager
        (thousand)
    """
    TR = 900
    TRE = 810
    SY0 = 820
    SY1 = 840
    SY2 = 870
    EX = 900
    MN = 1000