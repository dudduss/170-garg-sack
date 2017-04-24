#!/usr/bin/env python

from __future__ import division
import argparse


"""
===============================================================================
  Please complete the following function.
===============================================================================
"""

def basic_preprocess (P, M, N, items):
  print("here")
  i = 0
  newItems = []
  for i in range (0, N):
    if items[i][2] > P or items[i][3] > M or items[i][3] > items[i][4]:
      continue
    else:
      newItems.append(items[i])
  newItems = sorted(newItems, key = lambda item: (item[4] - item[3])/item[2], reverse = True)
  print("here1")
  return newItems

def constraint_checker (output, item, constraints):
  item_class = item[1]
  for constraint in constraints:
    if item_class in constraint:
      for val in output:
        if val[1] in constraint:
          return False
  return True

def knapsack(P, M, N, items, constraints):

  print(P)

  # resale_matrix = [[[0 for k in range(int(M))] for j in range(int(P))] for i in range(int(N))]
  # # items_matrix = [[[[] for k in range(M)] for j in range(P)] for i in range(N)]

  # for i in range(1,N+1,1):
  #     item = items[i-1]
  #     name,item_class, weight, cost, resale_value = items[i-1]
  #     for p in range(1,P+1,1):
  #       for m in range(1, M+1,1):
  #           if weight <= p and cost <= m:
  #             if ((resale_value + resale_matrix[i-1][p-weight][m-cost]) > resale_matrix[i-1][p][m]):
  #               if constraint_checker(items_matrix[i-1][p][m], item, constraints): #Constraint Check
  #                 resale_matrix[i][p][m] = resale_value + resale_matrix[i-1][p-weight][m-cost]
  #                 items_matrix[i][p][m] = items_matrix[i-1][p][m].append(item)
  #             else:
  #               resale_matrix[i][p][m] = resale_matrix[i-1][p][m]
  #               items_matrix[i][p][m] = items_matrix[i-1][p][m]
  #           else:
  #               resale_matrix[i][p][m] = resale_matrix[i-1][p][m]
  #               items_matrix[i][p][m] = items_matrix[i-1][p][m]

  # return (resale_matrix[N-1][P-1][M-1], items_matrix[N-1][P-1][M-1])


def output_converter(output):
  output_list = []
  for val in output:
    output_list.append(val[0])
  return output_list



def solve(P, M, N, C, items, constraints):
  """
  P = Pounds
  M = Dollars
  N = Number of Items
  C = Number of Constraints
  [item_name]; [class]; [weight]; [cost]; [resale value]
  [incompatible_class1, incompatible_class2, incompatible_class3]

  Write your amazing algorithm here.

  Return: a list of strings, corresponding to item names.
  """
  items = basic_preprocess(P, M, N, items) # Making sure no items are not profitable/don't weigh more than necessar 
  solution = knapsack(P, M, N, items, constraints) #Run knapsack to get the solution
  return output_converter(solution[1])

"""
===============================================================================
  No need to change any code below this line.
===============================================================================
"""

def read_input(filename):
  """
  P: float
  M: float
  N: integer
  C: integer
  items: list of tuples
  constraints: list of sets
  """
  with open(filename) as f:
    P = float(f.readline())
    M = float(f.readline())
    N = int(f.readline())
    C = int(f.readline())
    items = []
    constraints = []
    for i in range(N):
      name, cls, weight, cost, val = f.readline().split(";")
      items.append((name, int(cls), float(weight), float(cost), float(val)))
    for i in range(C):
      constraint = set(eval(f.readline()))
      constraints.append(constraint)
  return P, M, N, C, items, constraints

def write_output(filename, items_chosen):
  with open(filename, "w") as f:
    for i in items_chosen:
      f.write("{0}\n".format(i))

if __name__ == "__main__":

  parser = argparse.ArgumentParser(description="PickItems solver.")
  parser.add_argument("input_file", type=str, help="____.in")
  parser.add_argument("output_file", type=str, help="____.out")
  args = parser.parse_args()

  P, M, N, C, items, constraints = read_input(args.input_file)
  items_chosen = solve(P, M, N, C, items, constraints)
  write_output(args.output_file, items_chosen)
