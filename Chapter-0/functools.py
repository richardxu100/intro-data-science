from functools import partial

def exp(base, power):
    return base ** power 

two_to_the = partial(exp, 2)
square_of = partial(exp, power=2)

print(exp(4, 5))
print(two_to_the(7))
print('square of 31: {}'.format(square_of(31)))
