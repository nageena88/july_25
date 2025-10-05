# def student(name: str, age: int, add: str, city: str) -> None:
#     print(f"Student Name: {name}, Age: {age}, Address: {add}, City: {city}")


# student("John", 20, "123 Main St", "New York")
# student(12, "Alice", "456 Park Ave", "Los Angeles") # error
# student("Bob", 22, city="Chicago", add="789 Elm St")
# student(add="101 Oak St", city="San Francisco", name="Eve", age=21)

# student("Alice", 22, "456 Park Ave")
# -------------------------------------------------------------------------------


def student(name: str, age: int, add: str, city: str = "New York") -> None:
    print(f"Student Name: {name}, Age: {age}, Address: {add}, City: {city}")


student(
    "Alice",
    22,
    "456 Park Ave",
)
