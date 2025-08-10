# x = 0  # Initialize x to 0
# while x < 5:  # loop condition
#     print("Ram")
#     x += 1  # increment x


# x = 2
# while x < 21:
#     y = 1
#     while y < 11:
#         print(f"{x * y:4}", end=" ")
#         y += 1
#     print()
#     x += 1

Password = "my_password"
attempts = 0
while True:
    user_input = input("Enter password: ")
    if user_input == Password:
        print("Access granted")
        break
    else:
        attempts += 1
        print("Incorrect password. Try again.")
        if attempts >= 3:
            print("Too many attempts. Access denied.")
            break
