import random


names = ["Rukky", "Eammnuel", "Micaiah"]

def randomize_names():
    random.shuffle(names)
    return names


def get_random_number():
    return random.randint(1, 100)
