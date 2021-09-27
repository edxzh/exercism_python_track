def find_anagrams(word, candidates):
    return [anagram for anagram in candidates if is_anagram(anagram, word)]

def is_anagram(word_A, word_B):
    return sorted(word_A.lower()) == sorted(word_B.lower()) and word_A.lower() != word_B.lower()
