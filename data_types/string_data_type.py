st = "this is string data."
# print(type(st))
# print(st)
# print(st[0])
# print(st[-1])
# print(st[-2])

# st[0] = "T"
# print(st)

# del st[-1]
# print(st)

# # slicing

# print(st[0:4])
# print(st[5:])
# print(st[:5])
# print(st[-5:])
# print(st[::5])
# print(st[::-1])
#

# res = "ram" + " " + "chauhan"
# print(res)

# print(res[4::2])

# res = "ram" + 3
# res = "ram" * 3
# print(res)

# print(dir(st))
methods = [
    # "capitalize",
    # "casefold",
    # "center",
    # "count",
    # "encode",
    # "endswith",
    # "expandtabs",
    # "find",
    # "format",
    # "format_map",
    # "index",
    # "isalnum",
    # "isalpha",
    # "isascii",
    # "isdecimal",
    # "isdigit",
    # "isidentifier",
    # "islower",
    # "isnumeric",
    # "isprintable",
    # "isspace",
    # "istitle",
    # "isupper",
    "join",
    # "ljust",
    "lower",
    "lstrip",
    "maketrans",
    "partition",
    "removeprefix",
    "removesuffix",
    "replace",
    # "rfind",
    # "rindex",
    # "rjust",
    "rpartition",
    "rsplit",
    "rstrip",
    "split",
    "splitlines",
    # "startswith",
    "strip",
    "swapcase",
    "title",
    "translate",
    "upper",
    "zfill",
]

# print(len(methods))
# print(st)

# res = st.capitalize()
# print(res)
# print(st)


# print(res.casefold())

# print(st.center(50))
# print(st.center(50, "*"))
# print(st.rjust(50, "*"))
# print(st.ljust(50, "*"))


# print(st)
# print(st.count("is", 5))

# res = st.encode()
# print(res)
print(st)

# "endswith",
# res = st.endswith("data.")
# print(res)
# # "startswith",
# res = st.startswith("This")
# print(res)
# "expandtabs",
# res = "this\tis\tstring\tdata."
# sa = res.expandtabs(4)
# print(sa)
# print(sa[-9])
# "find",
# res = st.find("This")
# print(res)


# "format",
# name = "Ram"
# age = 24
# st1 = "My name is {1} and my age is {0}".format(name, age)
# print(st1)
# "format_map",
person = {"name": "Ram", "age": 24, "salary": 34000}
st2 = "My name is {name} and my age is {age}".format_map(person)
print(st2)

# "index",
# res = st.index("This")
# print(res)
