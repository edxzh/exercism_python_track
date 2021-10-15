TOTAL_HOURS = 24
TOTAL_MINUTES = 60

class Clock:
    def __init__(self, hour, minute):
        self.hour = (hour + minute // TOTAL_MINUTES) % TOTAL_HOURS
        self.minute = minute % TOTAL_MINUTES

    def __repr__(self):
        return "{:02d}:{:02d}".format(self.hour, self.minute)

    def __eq__(self, other):
        return (self.hour == other.hour) and (self.minute == other.minute)

    def __add__(self, minutes):
        return Clock(self.hour, self.minute + minutes)

    def __sub__(self, minutes):
        return Clock(self.hour, self.minute - minutes)

