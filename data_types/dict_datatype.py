# data = {
#     "name": "John",
#     "age": 30,
#     "city": "New York",
# }

# print(data)

# print(data["name"])  # Accessing value by key
# data["age"] = 31  # Modifying value by key
# print(data)
# data["country"] = "USA"  # Adding a new key-value pair
# print(data)

# del data["city"]  # Deleting a key-value pair
# print(data)

# print(type(data))  # Checking the type of the data structure

# print(len(data))  # Getting the number of key-value pairs

# print(dir(data))  # Listing all attributes and methods of the dictionary
methods = [
    "clear",
    "copy",
    "fromkeys",
    "get",
    "items",
    "keys",
    "pop",
    "popitem",
    "setdefault",
    "update",
    "values",
]

# s = ("math", "science", "history")
# d = {}
# d = d.fromkeys(s, 45)
# print(d)

data = {
    "name": "John",
    "age": 30,
    "city": "New York",
}

# name = data.get("name")
# print(name)

# salary = data.get("salary", 50000)
# print(salary)  # None
# print(data)

# items = list(data.items())
# print(items)

# for key, value in data.items():
#     print(key, value)

# keys = list(data.keys())
# print(keys)

# values = list(data.values())
# print(values)

# for x in data.keys():
#     print(x, data[x])

# for x in data.values():
#     print(x)
# for x in data:
#     print(x)

print(data)

# age = data.pop("age")
# print(age)
# print(data)

# item = data.popitem()
# print(item)
# print(data)

# item = data.popitem()
# print(item)
# print(data)

# info = data.setdefault("age", 25)
# print(info)
# print(data)

# salary = data.setdefault("salary", 50000)
# print(salary)
# print(data)

# data1 = {
#     "name": "Ram",
#     "age": 45,
#     "country": "USA",
#     "salary": 50000,
# }

# print(data1)

# data.update(data1)
# print(data)
# print(data1)
