# only if
# st = "I am a trainner of python"
# if "python" in st:
#     st = st.replace("python", "java")
# print(st)

# x = 10
# if x == 0:
#     print("x is zero")
#     exit(0)
# if x > 0:
#     print("x is positive")
# else:
#     print("x is negative or zero")

# if x == 0:
#     print("x is zero")
# elif x > 0:
#     print("x is positive")
# else:
#     print("x is negative")

# x = 10
# y, z = 90, 70
# if x < y and x < z:
#     print("x is smallest")
# elif y < z:
#     print("y is smallest")
# else:
#     print("z is smallest")

# z<y<x

# if x < y:
#     if x < z:
#         print("x is smallest")
#     else:
#         print("z is smallest")
# elif y < z:
#     print("y is smallest")
# else:
#     print("z is smallest")


# x, y = 10, 90

# res = x if x > y else y
# print("The greater number is:", res)

# if x > y:
#     res1 = x
# else:
#     res1 = y


# print("The greater number is:", res1)

x, y, z = 10, 90, 70
res = x if x > y and x > z else (y if y > z else z)
print("The greatest number is:", res)
