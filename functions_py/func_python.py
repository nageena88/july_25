# def my_function():
#     print("Hello from a function")


# my_function()
# my_function()


# add (no return, no argument)
def add():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print(a + b)


# sub (with return, no argument)
def sub():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    return a - b


# mul (no return, with argument)
def mul(a, b):
    print(a * b)


# div (with return, with argument)
def div(a, b):
    return a / b


# add()
# res = sub()
# print("Subtraction is:", res)
# mul(23, 3)
# res = div(23, 4)
# print("Division is:", res)

# x = sub()
# y = sub()
# res = div(x, y)
# print("Division is:", res)
