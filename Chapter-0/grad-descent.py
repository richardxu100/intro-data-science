def sum_of_squares(nums):
    return sum([num**2 for num in nums])

# print(sum_of_squares([2, 12, 3, 6]))

def difference_quotient(f, x, h):
    return (f(x + h) - f(x)) / h

def square(x):
    return x*x 

print(difference_quotient(square, 2, .00001))


from functools import partial
def derivative(x):
    return 2 * x 


derivative_estimate = partial(difference_quotient, square, h=.0000001)

import matplotlib.pyplot as plt 
x = range(-10, 10)
plt.title('Actual derivatives vs. Estimates')
plt.plot(x, list(map(derivative, x)), 'rx', label='Actual')
plt.plot(x, list(map(derivative_estimate, x)), 'b+', label='Estimate')
plt.legend(loc=9)
plt.show()
