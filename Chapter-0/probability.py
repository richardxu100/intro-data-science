import random

# def random_kid():
#     return choice(['boy', 'girl'])    

# # both_girls = 0

# probability density function
def uniform_pdf(x): 
    return 1 if x >= 0 and x < 1 else 0

# Cumulative distribution function
def uniform_cdf(x):
    """returns the prob. that a unfirom random variables is <= x"""
    if x < 0:   return 0
    elif x < 1: return x # P(x <= 0.4) = 0.4
    else:       return 1 

def bernoulli_trial(p): # p is the probability
    return 1 if random.random() < p else 0

def binomial(n, p):
    return sum(bernoulli_trial(p) for _ in range(n))

# print(binomial(10, .5))

from collections import Counter
from matplotlib.pyplot as plt
import math 

# def make_histogram(n, p, num_points):
#     data = [binomial(n,p) for _ in range(num_points)]

#     # Use a bar chart to show actual binomial samples
#     histogram = Counter(data)
#     plt.bar([x-.4 for x in histogram.keys()],
#             [v/num_points for v in histogram.values()],
#             .8,
#             color='0.75')
#     mu = n * p 
#     sigma = math.sqrt(n*p*math.sqrt(1-p))
#     xs = range(min(data, max(data)+1))
#     ys = [normal_cdf]