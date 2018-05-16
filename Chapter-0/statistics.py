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

print(iqr(my_list))

# Correlation
def covariance