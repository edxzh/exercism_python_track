def is_armstrong_number(number):
    num_str = str(number)
    result = (int(n) ** len(num_str) for n in num_str)

    return sum(result) == number
