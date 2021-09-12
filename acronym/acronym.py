def abbreviate(words: str) -> str:
    word_list = words.replace('-', ' ').replace('_', ' ').split()

    return ''.join([word[0].upper() for word in word_list])
