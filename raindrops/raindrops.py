dict = {
    3: 'Pling',
    5: 'Plang',
    7: 'Plong'
}

def convert(number):
    result = ""

    for factor in dict.keys():
        if number % factor == 0:
            result += dict.get(factor)
    else:
        if result == "":
            result = str(number)

    return result
