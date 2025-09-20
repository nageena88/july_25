# a = {1, 2, 3, 1, 2, 5, 6}
# print(a)
# print(type(a))

# a = set()
# print(a)
# print(type(a))

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(a)
print(b)
# print(a - b)
# print(b - a)
# print(a | b)
# print(a & b)
# print(a ^ b)

# print(dir(set))
methods = [
    "add",
    "clear",
    "copy",
    "difference",
    "difference_update",
    "discard",
    "intersection",
    "intersection_update",
    "isdisjoint",
    "issubset",
    "issuperset",
    "pop",
    "remove",
    "symmetric_difference",
    "symmetric_difference_update",
    "union",
    "update",
]

# x = {1, 2}
# x.add(3)
# print(x)

# x.add(2)
# print(x)

# print(a.difference(b))
# print(b.difference(a))

# a.difference_update(b)
# print(a)
# print(b)

# print(a.intersection(b))
# a.intersection_update(b)
# print(a)


# print(a.symmetric_difference(b))
# a.discard(3)
# print(a)

# print(a.isdisjoint(b))
# print(b.isdisjoint(a))

print(a.union(b))

a.update(b)
print(a)
