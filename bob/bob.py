def response(hey_bob: str):
    if (is_question(hey_bob) and is_yell(hey_bob)):
        return 'Calm down, I know what I\'m doing!'
    elif (is_address(hey_bob)):
        return 'Fine. Be that way!'
    elif (is_yell(hey_bob)):
        return 'Whoa, chill out!'
    elif (is_question(hey_bob)):
        return 'Sure.'
    else:
        return 'Whatever.'

def is_question(sentence):
    return sentence.strip().endswith('?')

def is_yell(sentence):
    return sentence.isupper()

def is_address(sentence):
    return sentence.strip() == ''
