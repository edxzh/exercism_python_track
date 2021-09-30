import math

def classify(number):
    if (number <= 0):
        raise ValueError('number has to be positive')

    square_root = int(math.sqrt(number))
    factors = []

    for i in range(1, square_root + 1):
        if (number % i == 0):
            factors += [i, number / i]
        else:
            pass

    # factor can't be itself
    sum_of_factors = sum(set(factors)) - number

    if (sum_of_factors == number):
        return 'perfect'
    elif (sum_of_factors < number):
        return 'deficient'
    else:
        return 'abundant'

