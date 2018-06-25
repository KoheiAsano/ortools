# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 15:14:29 2018

@author: Asako
"""


import sys
from ortools.constraint_solver import pywrapcp
from random import sample

solver = pywrapcp.Solver("schedule_shifts")

num_parts = 7
num_officer = 3#この場合0,1,2をOfficer、それ以降をPartに
num_workers = num_parts + num_officer
num_shifts = 10
num_days = 7
x1 = 5#土日の勤務人数
x2 = 3#平日の勤務人数
# [START]
# Create shift variables.
shifts = {}
for j in range(num_workers):
    for i in range(num_days):
        shifts[(j, i)] = solver.IntVar(0, num_shifts - 1, "shifts(%i,%i)" % (j, i))
#二次元配列変数群を作る
shifts_flat = [shifts[(j, i)] for j in range(num_workers) for i in range(num_days)]
#一次元化

workers = {}

for j in range(num_shifts):
    for i in range(num_days):
        workers[(j, i)] = solver.IntVar(0, num_workers - 1, "shift%d day%d" % (j,i))#shift'shifts' day'day'

        
#worker variable shift variable　を関係付ける
for day in range(num_days):
    workers_for_day = [workers[(j, day)] for j in range(num_shifts)]

    for j in range(num_workers):
        s = shifts[(j, day)]
        solver.Add(s.IndexOf(workers_for_day) == j)
        


for j in range(num_workers):
    solver.Add(solver.Sum([shifts[(j, i)] >= x1 for i in range(num_days)]) >= 3)
#現在は全員3回休むことにしている。4回にすると０通りに収束する。
"""
0,1,2をオフィサーとして、平日は最低一人、土日は最低二人の出勤をさせる
"""
#土日
for i in [0,6]:
    solver.Add(solver.Sum([shifts[(j, i)] < x1 for j in [0,1,2]]) == 2)
#平日
for i in [1,2,3,4,5]:
    solver.Add(solver.Sum([shifts[(j, i)] < x2 for j in [0,1,2]]) == 1)

"""
ナースそれぞれに出勤不可な曜日を指定。
0…火・土→2,6
1…木→4
2…水→3
3…日・金→0,5
4…月・火→1,2
5…木→4
6…金→5
7…日→0
8…火→2
9…土→6
"""
#土日の設定
for x in range(0,x1):
    solver.Add(shifts[(0,6)]!=x)
    solver.Add(shifts[(3,0)]!=x)
    solver.Add(shifts[(7,0)]!=x)
    solver.Add(shifts[(9,6)]!=x)
#平日の設定
for x in range(0,x2):
    solver.Add(shifts[(0,2)]!=x)
    solver.Add(shifts[(1,4)]!=x)
    solver.Add(shifts[(2,3)]!=x)
    solver.Add(shifts[(3,5)]!=x)
    solver.Add(shifts[(4,1)]!=x)
    solver.Add(shifts[(4,2)]!=x)
    solver.Add(shifts[(5,4)]!=x)
    solver.Add(shifts[(6,5)]!=x)
    solver.Add(shifts[(8,2)]!=x)

db = solver.Phase(shifts_flat, solver.CHOOSE_FIRST_UNBOUND,
                    solver.ASSIGN_MIN_VALUE)
# Create the solution collector.
solution = solver.Assignment()
solution.Add(shifts_flat)
collector = solver.AllSolutionCollector(solution)
time_limit_ms = solver.TimeLimit(10000)

solver.Solve(db, [time_limit_ms,collector])
print("Solutions found:", collector.SolutionCount())
print("Time:", solver.WallTime(), "ms")
print()

# Display a few solutions picked at random.
#index = range(collector.SolutionCount())
afs = []#sample(index,5)今は最後の番号一通りのみ表示
afs.append(collector.SolutionCount())
print(afs)





'''
勤務者のみ表示
０，６のx1以下と
1,2,3,4,5のx2以下表示
本来はシフトに入る人と、シフトの時間を表すものだったが、ここでは一旦出勤する人のみ求めるので出勤する人の番号だけ表示
'''
for sol in afs:
    print("Solution number" , sol, '\n')
    for i in range(num_days):
        print('\n')
        print("Day", i)
        for j in range(num_workers):
            if i == 0 or i == 6:
                if collector.Value(sol-1, shifts[(j, i)]) < x1:
                    #print("Part", j, "assigned to task",collector.Value(sol-1, shifts[(j, i)]))
                    if j == 0 or j == 1 or j == 2 :
                        print("Officer",j)
                    else:
                        print("Part", j)
            else:
                if collector.Value(sol-1, shifts[(j, i)]) < x2:
                    #print("part", j, "assigned to task",collector.Value(sol-1, shifts[(j, i)]))
                    if j == 0 or j == 1 or j == 2 :
                        print("Officer",j)
                    else:
                        print("Part", j)
    print()
"""

                        
"""
"""
                    if j == 0 or j == 1 or j == 2 :
                        print("Officer",j)
                    else:
                        print("Part", j)
"""
    