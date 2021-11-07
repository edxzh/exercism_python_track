def verse(n):
    if n == 0:
        return [
            "No more bottles of beer on the wall, no more bottles of beer.",
            "Go to the store and buy some more, 99 bottles of beer on the wall.",
        ]
    elif n == 1:
        return [
            "1 bottle of beer on the wall, 1 bottle of beer.",
            "Take it down and pass it around, no more bottles of beer on the wall.",
        ]
    elif n == 2:
        return [
            "2 bottles of beer on the wall, 2 bottles of beer.",
            "Take one down and pass it around, 1 bottle of beer on the wall.",
        ]
    else:
        return [
            f"{n} bottles of beer on the wall, {n} bottles of beer.",
            f"Take one down and pass it around, {n-1} bottles of beer on the wall.",
        ]

def recite(start, take=1):
    result = []

    for n in range(start, start - take, -1):
        v1, v2 = verse(n)
        result.extend([v1, v2, ""])

    return result[:-1]
