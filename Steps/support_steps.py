import random
import string


def generate_random_number_strings(length):
    result = ""
    for i in range(0, length):
        result += str(random.randint(0, 9))
    return result

def generate_random_letter_string(length):
    result = ""
    for i in range(0, length):
        result += str(random.choice(string.ascii_letters[random.randint(0, 5)]))
    return result