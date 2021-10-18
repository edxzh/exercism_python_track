def factors(num):
    factors = []
    f = 2

    while num > 1:
        while num % f == 0:
            num /= f
            factors.append(f)
        f += 1

    return factors
