from collections import Counter

def group_price(size: int):
    BASE_PRICE = 800
    DISCOUNTS = {
        1: 0,
        2: 5,
        3: 10,
        4: 20,
        5: 25,
    }

    return BASE_PRICE * size * (100 - DISCOUNTS[size]) // 100

def _groups(copies: Counter):
    result = Counter()

    while copies:
        group = Counter(copies.keys())
        result[len(group)] += 1
        copies -= group

    return result

def total(basket):
    copies = Counter(basket)
    groups = _groups(copies)
    a = min(groups[3], groups[5])
    groups.update({3: -a, 5: -a, 4: 2 * a})
    return sum(group_count * group_price(group_size) for group_size, group_count in groups.items())
