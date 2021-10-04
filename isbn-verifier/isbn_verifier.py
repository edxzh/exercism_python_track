def is_valid(isbn):
    nums = list(isbn.replace("-", ""))

    if len(nums) != 10: return False

    if nums[-1] == "X": nums[-1] = "10"

    if not all([c.isdigit() for c in nums]): return False

    return sum(int(e) * (len(nums) - index) for index, e in enumerate(nums)) % 11 == 0
