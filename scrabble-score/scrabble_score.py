SCORES = {
    "AEIOULNRST": 1,
    "DG": 2,
    "BCMP": 3,
    "FHVWY": 4,
    "K": 5,
    "JX": 8,
    "QZ": 10,
}

SCORES_MAP = { letter: value for letters, value in SCORES.items() for letter in letters }

def score(word: str) -> int:
    return sum(SCORES_MAP[letter] for letter in word.upper())
