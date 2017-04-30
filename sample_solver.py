#!/usr/bin/env python

from __future__ import division
import argparse
import math
import sys
import random

"""
===============================================================================
  Please complete the following function.
===============================================================================
"""

def solve(P, M, N, C, items, constraints):
  """
  P = Pounds
  M = Dollars
  N = Number of Items
  C = Number of Constraints
  [item_name]; [class]; [weight]; [cost]; [resale value]
  [incompatible_class1, incompatible_class2, incompatible_class3]

  problem1 = items[39:] = 50569290
  problem2 = items[20:] = 2001095565
  problem3 = items[40:] = 202008987

  Write your amazing algorithm here.

  Return: a list of strings, corresponding to item names.
  """

  # P = int(math.floor(P))
  # M_original = M
  # M = int(math.floor(M))
  items = basic_preprocess(P, M, N, items)
  items = items[39:]
  N = len(items)
  max_output = []
  output = []
  weight = 0
  spent = 0
  value = 0
  max_spent =  0
  max_val = 0
  count = 0
  item_position = 0
  for item in items:
    max_spent += item[3]
    max_val += item[4]
  max_Profit = 0

  while count < 7 and len(items) > 0 and (max_Profit <= (M - max_spent + max_val)):
    print("checking")
    sys.stdout.flush()
    first_item = items.pop(0)
    weight += first_item[2]
    spent += first_item[3]
    value += first_item[4]
    max_spent -= item[3]
    max_val -= item[4]
  
    for item in items:
      if (weight + item[2] <= P and spent + item[3] <= M and constraint_checker(output, item, constraints)):
        weight += item[2]
        spent += item[3]
        value += item[4]
        output.append(item)

    if (max_Profit < M - spent + value):
      max_Profit = M - spent + value
      max_output = output
      print (max_Profit, item_position)
      count += 1

    item_position += 1
    weight = 0
    spent = 0
    value = 0
    output = []
  

  return output_converter(max_output)


def max_summations(P, M, N, items):
  max_P = 0
  max_M = 0
  max_V = 0
  top_P = 0
  low_P = float("inf")
  top_M = 0
  low_M = float("inf")
  for i in range (0, N):
    max_P = max_P + items[i][2]
    max_M = max_M + items[i][3]
    max_V = max_V + items[i][4]
    if top_P < items[i][2]:
      top_P = items[i][2]
    if low_P > items[i][2] and items[i][2] != 0:
      low_P = items[i][2]
    if top_M < items[i][3]:
      top_M = items[i][3]
    if low_M > items[i][3] and items[i][3] != 0:
      low_M = items[i][3]
  return (max_P, max_P, max_V, top_P, low_P, top_M, low_M)


# def knapsack(items, N, M, P, constraints):

#   resale_matrix = [[[0 for k in range(M//10000)] for j in range(P//10000)] for i in range(N)]
#   # items_matrix = [[[[] for k in range(M//10000)] for j in range(P//10000)] for i in range(N)]

#   # print("construction finished")
#   # for i in range(1,N+1,1):
#   #     name,item_class, weight, cost, resale_value = items[i-1]
#   #     for p in range(1,P+1,1):
#   #       for m in range(1, M+1,1):
#   #           if weight <= p and cost <= m and constraint_checker(items_matrix[i][p][m], items[i], constraints) :
#   #             #Make the constraint check here 
#   #             if ((resale_value + resale_matrix[i-1][p-weight][m-cost]) > resale_matrix[i-1][p][m]):
#   #                 resale_matrix[i][p][m] = resale_value + resale_matrix[i-1][p-weight][m-cost]
#   #                 # items_matrix[i][p][m] = items_matrix[i-1][p][m].append(item)
#   #             else:
#   #               resale_matrix[i][p][m] = resale_matrix[i-1][p][m]
#   #               # items_matrix[i][p][m] = items_matrix[i-1][p][m]
#   #           else:
#   #               resale_matrix[i][p][m] = resale_matrix[i-1][p][m]
#   #               # items_matrix[i][p][m] = items_matrix[i-1][p][m]

#   # return resale_matrix[N-1][P-1][M-1]


def basic_preprocess (P, M, N, items):
  newItems = []
  for i in range (0, N):
    if items[i][2] > P or items[i][3] > M or items[i][3] >= items[i][4]:
      continue
    else:
      # newItem = (items[i][0], items[i][1], int(math.ceil(items[i][2])), int(math.ceil(items[i][3])), items[i][4])
      # newItems.append(newItem)
      newItems.append(items[i])
  newItems = sorted(newItems, key=lambda item: (item[4] - item[3]), reverse=True)
  return newItems



def constraint_checker (output, item, constraints):
  item_class = item[1]
  for constraint in constraints:
    if item_class in constraint:
      for val in output:
        if val[1] in constraint:
          return False
  return True

def output_converter(output):
  output_list = []
  for val in output:
    output_list.append(val[0])
  return output_list
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
