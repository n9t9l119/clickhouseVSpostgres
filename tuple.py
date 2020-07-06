import random, string


def random_word(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def create_tuple():
    tuple_lst = []
    for i in range(0, 100000):
        tuple_lst.append(
            (random.randint(0, 100000), random_word(10), random_word(15), random_word(20), random_word(25),
             random_word(30)))
        if i % 10000 == 0:
            print(i)
    return tuple_lst
