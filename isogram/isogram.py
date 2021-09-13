def is_isogram(string: str):
    alpha_letters = [letter for letter in string.lower() if letter.isalpha()]

    return len(alpha_letters) == len(set(alpha_letters))
