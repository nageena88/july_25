# print("Ram", end=" ")
# print("Chauhan")


for x in range(5):
    for y in range(5):
        if x < y:
            break
        print("*", end="")
    print()


x, y = 12, 4565

# print("x = {1}, y = {0}".format(y, x))
print(f"x = {x:04}, y = {y:04}")
# print(f"{x*y}")
