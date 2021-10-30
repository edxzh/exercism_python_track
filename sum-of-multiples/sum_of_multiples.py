def sum_of_multiples(limit, multiples):
    return sum(
        set(
            num
            for num in range(limit)
            for multiple in multiples
            if (multiple != 0) and (num % multiple == 0)
        )
    )
