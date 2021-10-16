class PhoneNumber:
    def __init__(self, number):
        digits = [n for n in number if n.isdigit()]

        self.number = self.parse_number_from(digits)
        self.area_code = self.number[:3]

    def parse_number_from(self, digits):
        if (digits[0] == '1'):
            digits = digits[1:]

        if (len(digits) != 10 or int(digits[0]) < 2 or int(digits[3]) < 2):
            raise ValueError('Invalid')

        return "".join(digits)

    def pretty(self):
        return f'({self.area_code})-{self.number[3:6]}-{self.number[6:]}'
