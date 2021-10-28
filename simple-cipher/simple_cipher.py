import string
import secrets
from itertools import cycle

class Cipher:
    def __init__(self, key=None):
        self.key = ''.join(secrets.choice(string.ascii_lowercase)
                           for _ in range(100)) if not key else key

    def encode(self, text):
        return ''.join(string.ascii_lowercase[(ord(a) % 97 + ord(b) % 97) % 26] for a, b in zip(text, cycle(self.key)))

    def decode(self, text):
        return ''.join(string.ascii_lowercase[(ord(a) % 97 - ord(b) % 97) % 26] for a, b in zip(text, cycle(self.key)))
