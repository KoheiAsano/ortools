from __future__ import print_function
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 19:47:03 2018

@author: Asako
"""

"""


"""

import sys
from ortools.constraint_solver import pywrapcp
from random import sample

#土日一日とする
def main(worker_num,shift_num):
    # Creates the solver.
    solver = pywrapcp.Solver("Shift")
    # Creates the variables.
    # The array index is the column, and the value is the row.
    workers = [solver.IntVar(0, shift_num-1, "x%i" % i) for i in range(worker_num)]
    #クイーンの取りうる位置を作成
    # Creates the constraints.
    #1,2,3,4,5を出勤として、それぞれ一人ずつ
    """
    for x in [1,2,3,4,5]:
        solver.Add(solver.Sum([workers[j] == x  for j in range(worker_num)]) == 1)
    """
    solver.Add(solver.Sum([workers[j] == 1  for j in range(worker_num)]) == 5)
    #0,1,2をOfficerとして、2人選ばれるように
    solver.Add(solver.Sum([workers[j] == 1  for j in [0,1,2]]) == 2)
    db = solver.Phase(workers,
                                        solver.CHOOSE_FIRST_UNBOUND,
                                        solver.ASSIGN_MIN_VALUE)
    solution = solver.Assignment()
    solution.Add(workers)
    collector = solver.AllSolutionCollector(solution)
    solver.Solve(db, [collector])
    print("Solutions found:", collector.SolutionCount())
    print("Time:", solver.WallTime(), "ms")
    print()
    index = range(collector.SolutionCount())
    afs = sample(index,5)#最後の番号一通りのみ表示afs.append(collector.SolutionCount())
    print(afs)
    for sol in afs:
        print("Solution number" , sol, '\n')
        for j in range(worker_num):
            if collector.Value(sol, workers[j]) ==1:
                if j == 0 or j == 1 or j == 2 :
                    print("Officer",j)
                else:
                    print("Part", j)
    print()
# By default, solve the 8x8 problem.
worker_num = 10
shift_num = 2

if __name__ == "__main__":
    if len(sys.argv) > 1:
        worker_num = int(sys.argv[1])
    main(worker_num,shift_num)