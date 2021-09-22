FIRST_SENTENCE = 'a Partridge in a Pear Tree.'

GIFTS = [
    'twelve Drummers Drumming, ',
    'eleven Pipers Piping, ',
    'ten Lords-a-Leaping, ',
    'nine Ladies Dancing, ',
    'eight Maids-a-Milking, ',
    'seven Swans-a-Swimming, ',
    'six Geese-a-Laying, ',
    'five Gold Rings, ',
    'four Calling Birds, ',
    'three French Hens, ',
    'two Turtle Doves, and ',
    FIRST_SENTENCE,
]

ORDINALS = [
    'first',
    'second',
    'third',
    'fourth',
    'fifth',
    'sixth',
    'seventh',
    'eighth',
    'ninth',
    'tenth',
    'eleventh',
    'twelfth',
]

VERSE_PATTERN = \
    'On the {nth} day of Christmas my true love gave to me: {sentence}'

def _get_sentence(index):
  if index == 1:
    return FIRST_SENTENCE

  return ''.join(GIFTS[-index:])

def recite(start_verse, end_verse):
    return [
        VERSE_PATTERN.format(nth=ORDINALS[index], sentence=_get_sentence(index + 1))
        for index in range(start_verse - 1, end_verse)]
