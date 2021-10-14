class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ", "")

    def valid(self):
        if len(self.card_num) <= 1:
            return False

        if not self.card_num.isnumeric():
            return False

        return sum(self.double_digit(int(c)) if i % 2 == 1 else int(c) for i, c in enumerate(self.card_num[::-1])) % 10 == 0

    def double_digit(self, original_num):
        if (original_num * 2 > 9):
            return original_num * 2 - 9

        return original_num * 2
