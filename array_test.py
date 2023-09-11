import random


class Gauge:

    @staticmethod
    def reading():
        return random.randrange(1,10)


class Reading():
    def __init__(self, size: int):
        self._size = size

    def create_reading_structure(self):
        self._reading_structure= {number:None for number in range(self._size)}
        return self._reading_structure


if __name__ == "__main__":
    readings = Reading(5).create_reading_structure()
    print(readings)

    readings[0] = Gauge.reading()
    readings[1] = Gauge.reading()
    readings[2] = Gauge.reading()
    readings[3] = Gauge.reading()
    readings[4] = Gauge.reading()
    print(readings)
