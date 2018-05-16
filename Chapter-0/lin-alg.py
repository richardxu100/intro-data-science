"""Vectors
# One dimensional collections of numbers (as in, there's only one data point)
"""
height_weight_age = [70,
                     170,
                     40]

grades = [95,
          80,
          75,
          62]

def vector_add(v, w):
    return [v_i + w_i for v_i, w_i in zip(v, w)]

def vector_subtract(v, w):
    return [v_i - w_i for v_i, w_i in zip(v, w)]

def vector_mult(v, w):
    return [v_i * w_i for v_i, w_i in zip(v, w)]

def dot_product(v, w):
    return sum([v_i * w_i for v_i, w_i in zip(v, w)])

def sum_of_squares(v):
    return dot_product(v, v)

import math 
def magnitude(v):
    return math.sqrt(sum_of_squares(v))

def squared_distance(v, w):
    return sum_of_squares(vector_subtract(v, w))

def distance(v, w):
    # return math.sqrt(squared_distance(v, w))
    return magnitude(vector_subtract(v,w))

# print('Distance between [0, 0] and [1, 1]: {}'.format(distance([1,1], [2,2])))

vector1 = [2, 4, 6]
vector2 = [1, 5, 3]
vector3 = [10, 51, 33]

# sum_vecs = vector_add(, )
sub_vecs = vector_subtract([2, 4, 6], [1, 5, 3])

from functools import reduce

def vector_sum(vectors):
    return reduce(vector_add, vectors)

# print(vector_sum([vector1, vector2, vector3]))
# print(dot_product(vector1, vector2))
# print(magnitude(vector2))

"""Matrices
# 2d collections of numbers
"""

A = [[1,2,3],
     [4,5,6]]

B = [[1,2],
     [3,4],
     [5,6]]

def shape(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) # can maybe implement a check if the matrix exists
    return rows, cols

# print(shape(A))

def make_matrix(entry_func, num_rows, num_cols):
    return [[entry_func(i, j)
            for i in range(num_cols)]
            for j in range(num_rows)]

def is_diagonal(i, j):
    return 1 if i == j else 0

# print(make_matrix(is_diagonal, 3, 4))

"""Statistics
"""
def median(nums):
    sorted_nums = sorted(nums)
    if len(sorted_nums) % 2 == 0:
        return average([sorted_nums[int(len(sorted_nums)/2)-1], 
                        sorted_nums[int(len(sorted_nums)/2)]])
    else:
        return sorted_nums[len(sorted_nums) // 2]

def average(nums):
    return sum(nums) / len(nums)

def quantile(nums, quant):
    sorted_nums = sorted(nums)
    quant_index = int(quant*len(sorted_nums))
    return sorted_nums[quant_index]
    
# print(median([43, 13, 17, 132]))
# print(quantile(range(100), .90))

from collections import Counter 
def mode(nums):
    counter = Counter(nums)
    max_count = max(counter.values())
    max_keys = []
    for key in counter.keys():
        if counter.get(key) == max_count:
            max_keys.append(key)
    return max_keys

my_list = [23, 23, 10, 15, 6, 23, 10, 10]
# print(mode(my_list))

def range(nums):
    return max(nums) - min(nums)

# print(range(my_list))

def de_mean(nums): # deviations from a mean
    mean = average(nums)
    return [num - mean for num in nums]

# print(de_mean(my_list))

def variance(nums):
    return sum_of_squares(nums) / (len(nums) - 1)

def sum_of_squares(nums):
    total = 0
    for num in nums:
        total += num**2
    return total

# print(sum_of_squares([3, 4, 5]))

# print(variance(my_list))

from math import sqrt 
def std(nums):
    return sqrt(variance(nums))

# print(std(my_list))

def iqr(nums):
    return quantile(nums, .75) - quantile(nums, .25)

# print(iqr(my_list))

"""Correlation
* Note robust (outliers really influence correlation)
* A value between -1 (perfect anti-correlation) and 1 (perfect correlation)
"""


def covariance(x, y):
    # Covariance measures how two variables vary in tandem from their means
    n = len(x)
    return dot_product(de_mean(x), de_mean(y)) / (n-1)

# covariance(num_friends, daily_minutes)

def correlation(x, y):
    std_x = std(x)
    std_y = std(y)
    if std_x > 0 and std_y > 0:
        return covariance(x,y) / (std_x * std_y)
    else:
        return 0 # when either std_x or std_y is 0.

# correlation(num_friends, daily_minutes)

