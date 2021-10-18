TOTAL_SQUARES = 64

def valid(f):
    def wrapper(number):
        if (0 < number <= TOTAL_SQUARES):
            return f(number)
        else:
            raise ValueError('Invalid')

    return wrapper

@valid
def square(number):
    return 2 ** (number - 1)


def total():
    return 2 ** TOTAL_SQUARES - 1
