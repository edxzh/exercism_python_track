def valid(f):
    return lambda s: 2 * max(s) < sum(s) and f(s)

@valid
def equilateral(sides):
    return len(set(sides)) == 1


@valid
def isosceles(sides):
    return len(set(sides)) <= 2

@valid
def scalene(sides):
    return len(set(sides)) == 3
