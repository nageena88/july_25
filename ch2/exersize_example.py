str1 = "This is a python class."
sub_str = "Python"
value = False
for x in str1.split():
    if sub_str == x:
        value = True
        break


print(value)
