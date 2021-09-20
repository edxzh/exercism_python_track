def add_prefix_un(word):
    '''

    :param word: str of a root word
    :return:  str of root word with un prefix

    This function takes `word` as a parameter and
    returns a new word with an 'un' prefix.
    '''

    return 'un' + word


def make_word_groups(vocab_words):
    '''

    :param vocab_words: list of vocabulary words with a prefix.
    :return: str of prefix followed by vocabulary words with
             prefix applied, separated by ' :: '.

    This function takes a `vocab_words` list and returns a string
    with the prefix  and the words with prefix applied, separated
     by ' :: '.
    '''

    prefix = vocab_words[0]
    vocab_words_with_prefix = list(
        map(lambda word: prefix + word if word != prefix else word, vocab_words))

    return ' :: '.join(vocab_words_with_prefix)


def remove_suffix_ness(word):
    '''

    :param word: str of word to remove suffix from.
    :return: str of word with suffix removed & spelling adjusted.

    This function takes in a word and returns the base word with `ness` removed.
    '''
    adjective = word.replace('ness', '')

    if (adjective[-1] == 'i'):
        adjective = adjective[:-1] + 'y'

    return adjective


def noun_to_verb(sentence, index):
    '''

    :param sentence: str that uses the word in sentence
    :param index:  index of the word to remove and transform
    :return:  str word that changes the extracted adjective to a verb.

    A function takes a `sentence` using the
    vocabulary word, and the `index` of the word once that sentence
    is split apart.  The function should return the extracted
    adjective as a verb.
    '''

    vocab_words = sentence.replace('.', '').split(' ')
    noun = vocab_words[index]

    return noun + 'en'
