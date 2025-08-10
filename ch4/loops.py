# for loops
for x in range(5, 10):
    print("Ram")

# while loops

# lst = list(range(5))  # start_val, end_val, step_val = 0, 5, 1
# print(lst)

# lst = list(range(5, 25))  # start_val, end_val, step_val = 5, 25, 1
# print(lst)

# x = list(range(5, 25, 3))  # start_val, end_val, step_val = 5, 25, 3
# print(x)

# # start_val, end_val, step_val

# x = list(range(10, 0, -1))  # start_val, end_val, step_val = 10, 0, -1
# print(x)

# table = list(range(2, 21, 2))  #   start_val, end_val, step_val = 2, 21, 2
# print(table)

# for x in range(1, 11):
#     print(x * 5)

# for x in range(1, 101):
#     if not x % 2:  # if  x%2 == 0
#         print(x, end=" ")
# print()  # To ensure the output ends with a newline
# x = (1,)

# if x:
#     print("x is truthy")
# else:
#     print("x is falsy")

for x in range(5):
    for y in range(5):
        print("*", end="")
    print()  # To move to the next line after printing a row

# x, y = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)]
# x, y = [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4)]
# x, y = [(2, 0), (2, 1), (2, 2), (2, 3), (2, 4)]
# x, y = [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4)]
# x, y = [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]


# for x in range(5):
#     for y in range(5):
#         if x == y and x == 2:
#             print("R", end="")
#         else:
#             print("*", end="")
#     print()


# for x in range(2, 21):
#     for y in range(1, 11):
#         print(f"{x * y:4}", end=" ")
#     print()


# for x in range(5):
#     for y in range(x + 1):
#         print("*", end="")
#     print()


# for x in range(5):
#     for k in range(5 - x):
#         print(" ", end="")
#     for y in range(x + 1):
#         print("*", end="")
#     print()

# for x in range(5):
#     for k in range(5 - x):
#         print(" ", end="")
#     for y in range(x + 1):
#         print("* ", end="")
#     print()


# for x in range(5):
#     for y in range(5 - x):
#         print("*", end="")
#     print()

# for x in range(5):
#     for y in range(x, 5):
#         print("*", end="")
#     print()


# 5 = 5
# 4 = 4


# for x in range(5):
#     for y in range(5):
#         if x < y:
#             break
#         print("*", end="")
#     print()

import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# random.shuffle(numbers)
# print(numbers)
# for x in numbers:
#     print(x * 2)

# even = []
# odd = []
# div3 = []
# for x in numbers:
#     if x % 2 == 0:
#         even.append(x)
#     else:
#         odd.append(x)
#     if x % 3 == 0:
#         div3.append(x)
# print("Even numbers:", even)
# print("Odd numbers:", odd)
# print("Numbers divisible by 3:", div3)
# t = 0
# for x in div3:
#     t += x
# print("Sum of numbers divisible by 3:", t)
