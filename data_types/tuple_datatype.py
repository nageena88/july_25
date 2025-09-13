# t = ()
# print(type(t))  # <class 'tuple'>
# print(t)

# t = (1,)
# print(type(t))  # <class 'tuple'>
# print(t)

t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(t)
# print(type(t))

# print(t[0])
# print(t[-1])

# t[0] = 100
# print(t)

# del t[0]

# print(dir(t))

# counter_item = t.count(10)
# print(counter_item)

# index_item = t.index(5)
# print(index_item)

even = [i for i in t if i % 2 == 0]
even = tuple(even)
print(even)
print(t)
