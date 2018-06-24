# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 11:56:10 2018

@author: Asako
"""
from ortools.linear_solver import pywraplp
from Class import Cnd,Slr
from numpy import *
import csv


#basic options
num_workers = 10
num_days = 7
num_weekdays = 5
num_weekends = 2

#  workerSalary=[w0,w1,w2,w3,w4,w5,w6,w7,w8,w9]
workerSalary = [Slr.MN, Slr.MN,Slr.MN, Slr.TRE,Slr.SY0, Slr.SY0, Slr.SY0,Slr.SY1, Slr.SY2, Slr.EX]

def create_weekShift(desiredShift,Feedback):
    #create solver
    solver = pywraplp.Solver('ShiftMIPSolver', pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
    
    #create variables
    x = {}
    for i in range(num_workers):
        for j in range(num_days):
            x[i, j] = solver.BoolVar('x[%i,%i]' % (i, j))#0が欠勤、1が出勤

    #create objective function
    solver.Minimize(solver.Sum([workerSalary[i].value * desiredShift[i][j].value *Feedback[i] * x[i,j] for i in range(num_workers) for j in range(num_days)]))
    
    #create 3 constraints below.
    """
    constraint1:Each day is assigned to 3 workers in weekdays,5 workers in weekends
    
    constraint2:Each worker is assigned to at most 4 days, at least 2days
    
    constraint3:Each day there needs at least one manager in weekdays, two manager in weekends.
    (HACK 0 and 1 and 2 is index of manager, please check out workerSalary)
    
    """
    #constraint1
    for j in [0, 1, 2, 3, 4]:
        solver.Add(solver.Sum([x[i, j] for i in range(num_workers)]) == 3)
    for j in [5,6]:
        solver.Add(solver.Sum([x[i, j] for i in range(num_workers)]) == 5)
    #constraint2
    for i in range(num_workers):
        solver.Add(solver.Sum([x[i, j] for j in range(num_days)]) <= 4)
    for i in range(num_workers):
        solver.Add(solver.Sum([x[i, j] for j in range(num_days)]) >= 2)
        
    #constraint3
    for j in [0,1,2,3,4]:
        solver.Add(solver.Sum([x[0,j], x[1,j],x[2,j]]) >= 1)
    for j in [5,6]:
        solver.Add(solver.Sum([x[0,j], x[1,j],x[2,j]]) >= 2)
        
    #optimize
    sol = solver.Solve()
    
    #out put Shift
    for j in range(num_days):
        for i in range(num_workers):
            if x[i, j].solution_value() > 0:
                print ('Worker {} assigned to day {} Cost = {}'.format(i,j,workerSalary[i].value * desiredShift[i][j].value *Feedback[i]))
        print("\n")
        
    #create each worker's shift, count worker's continuous shift.
    continuouscount = array([])
    Shift = []
    for i in range(num_workers):
        PersonalShift = []
        for j in range(num_days):
            PersonalShift.append(int(x[i,j].solution_value()))
        print("Worker {} 一週間の勤務数合計{} days".format(i,PersonalShift.count(1)))
        workdays = [k for k, x in enumerate(PersonalShift) if x == 1]
        print("勤務曜日{}".format(workdays))
        Shift.append(PersonalShift)
        con = 0
        for y in range(len(workdays)-1):
            if workdays[y+1]-workdays[y]==1:
                con += 1
        continuouscount = append(continuouscount,con)
    continuouscount = continuouscount / 10
    print("Worker毎の連勤数によるFeedback {}".format(continuouscount))
    print("\n")
    
    
    #count defference between worker's desire and real Shift.
    scorelist = array([])
    for i in range(num_workers):
        score = 0
        for j in range(num_days):
            if desiredShift[i][j] == Cnd.P and Shift[i][j] ==1:
                score +=3
        scorelist = append(scorelist,score)
    scorelist = scorelist /10
    print("公休希望(P)出したけど出勤した日数によるFeedback\n ",scorelist)
    
    Feedback = Feedback + scorelist + continuouscount
    print("次のFeedback rate{}".format(Feedback))
    lastfeed = array([1,1,1,1,1,1,1,1,1,1]) + scorelist + continuouscount
    return Feedback,lastfeed


def call_desired():
    f = open('weekshift.csv', 'r')
    reader = csv.reader(f)
    header = next(reader)
    tmp = []
    week0 = []
    week1 = []
    week2 = []
    week3 = []
    Input = {"W":Cnd.W,"OK":Cnd.OK,"P":Cnd.P,"IM":Cnd.IM}
    for r in reader:
        tmp = r[:7]
        tmpdesire = [Input[tmp[0]],Input[tmp[1]],Input[tmp[2]],Input[tmp[3]],Input[tmp[4]],Input[tmp[5]],Input[tmp[6]]]
        week0.append(tmpdesire)
        tmp = r[7:14]
        tmpdesire = [Input[tmp[0]],Input[tmp[1]],Input[tmp[2]],Input[tmp[3]],Input[tmp[4]],Input[tmp[5]],Input[tmp[6]]]
        week1.append(tmpdesire)
        tmp = r[14:21]
        tmpdesire = [Input[tmp[0]],Input[tmp[1]],Input[tmp[2]],Input[tmp[3]],Input[tmp[4]],Input[tmp[5]],Input[tmp[6]]]
        week2.append(tmpdesire)
        tmp = r[21:]
        tmpdesire = [Input[tmp[0]],Input[tmp[1]],Input[tmp[2]],Input[tmp[3]],Input[tmp[4]],Input[tmp[5]],Input[tmp[6]]]
        week3.append(tmpdesire)
    
    MShift = [week0,week1,week2,week3]
    return MShift