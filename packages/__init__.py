import random

# print(dir(random))

methods = [
    "choice",
    "choices",
    "gauss",
    "getrandbits",
    "getstate",
    "randbytes",
    "randint",
    "random",
    "randrange",
    "sample",
    "seed",
    "setstate",
    "shuffle",
    "triangular",
    "uniform",
]

# print(random.random())

# print(random.randint(1, 100))

# print(random.randrange(1, 10, 2))

# print(random.choice(["apple", "banana", "cherry"]))

# print(random.choices(["apple", "banana", "cherry"], k=2))

# print(random.sample(["apple", "banana", "cherry"], k=2))

# random.seed(1)
# rand_list = []
# for _ in range(10):
#     rand_list.append(random.randint(1, 100))

# print(rand_list)

# random.shuffle(rand_list)
# print(rand_list)
# random.seed(1)
# lst = list(range(1, 11))
# print(lst)
# random.shuffle(lst)
# print(lst)

print(random.uniform(1, 10))
