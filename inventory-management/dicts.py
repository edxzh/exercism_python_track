from collections import Counter

def create_inventory(items):
    '''

    :param items: list - list of items to create an inventory from.
    :return:  dict - the inventory dictionary.
    '''

    return Counter(items)


def add_items(inventory, items):
    '''

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return:  dict - the inventory dictionary update with the new items.
    '''

    c = Counter(inventory)
    c.update(items)

    return c


def delete_items(inventory, items):
    '''

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to remove from the inventory.
    :return:  dict - updated inventory dictionary with items removed.
    '''

    c = Counter(inventory)
    for item in items:
        if c[item] > 0:
            c.subtract({ item: 1 })

    return c


def list_inventory(inventory):
    '''

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    '''

    c = Counter(inventory)

    return [x for x in c.items() if x[1] > 0]
