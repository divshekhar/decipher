import random


def random_key(key_length: int) -> list[int]:
    key = list()
    while len(key) < key_length:
        k = random.randint(1, 9)
        if k not in key:
            key.append(k)
    return key
