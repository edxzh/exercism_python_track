import re
from collections import Counter

def count_words(sentence):
    sentence_list = re.split('[\s,:!&@$%^._]', sentence.lower())
    sentence_list = [x.strip('\'') for x in sentence_list if x != '']

    return Counter(sentence_list)
