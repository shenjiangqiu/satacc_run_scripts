import random
import string
from time import time


def same_str_on(a, b):
    if len(a) != len(b):
        return False
    letter_dict = dict()
    for a_i, b_i in zip(a, b):
        letter_dict[a_i] = letter_dict.get(a_i, 0) + 1
        letter_dict[b_i] = letter_dict.get(b_i, 0) - 1
    # return all(v == 0 for v in letter_dict.values())
    return all(map(lambda v: v == 0, letter_dict.values()))


def same_str_onsqre(a, b):
    if len(a) != len(b):
        return False
    b_list = list(b)
    for a_i in a:
        i = 0
        found = False
        while i < len(b_list):
            if a_i == b_list[i]:
                b_list[i] = None
                found = True
                break
            i += 1
        if not found:
            return False
    return True


def same_str_ologn(a, b):
    if len(a) != len(b):
        return False
    b_list = list(b)
    a_list = list(a)
    a_list.sort()
    b_list.sort()
    return a_list == b_list


# generate a random string of length 10000


def random_str(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))


a = random_str(50000)
b = random_str(50000)

current_time = time()
same_str_on(a, b)
print("time for O(n): ", time() - current_time)

current_time = time()
same_str_onsqre(a, b)
print("time for O(n^2): ", time() - current_time)

current_time = time()
same_str_ologn(a, b)
print("time for O(nlogn): ", time() - current_time)
# test
