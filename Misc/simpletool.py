import random

feet_to_mile = 200
meter_to_kilometer = 1000

beatles = ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Star"]


def get_file_ext(filename):
    return filename[filename.index(".") + 1]


def roll_dice(num):
    return random.randint(1, num)
