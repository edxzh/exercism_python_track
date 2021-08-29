import string
import random


class Robot:
    def __init__(self):
        self.generate_name()

    def generate_name(self):
        random.seed()

        alphabet = "".join(random.SystemRandom().choice(string.ascii_uppercase) for _ in range(2))
        digits = "".join(random.SystemRandom().choice(string.digits) for _ in range(3))

        self.name = f"{alphabet}{digits}"

    def reset(self):
        self.generate_name()
