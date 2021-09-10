def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('invalid')

    return len([n for i, n in enumerate(strand_a) if n != strand_b[i]])
