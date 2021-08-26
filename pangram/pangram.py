import string

def is_pangram(sentence):
    str_list = [l for l in set(sentence.lower()) if l.lower() in string.ascii_lowercase]

    return len(str_list) == 26
