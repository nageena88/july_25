from pathlib import Path

file_path = Path(__file__)

# print(file_path)
parent_path = file_path.parent
# print(parent_path)
data_path = parent_path.joinpath("data")
# print(data_path)

# print(data_path.exists())
# print(data_path.is_dir())
# print(data_path.is_file())

# lst = parent_path.rglob("*")
# print(list(lst))

data_file = data_path.glob("*")

for f in data_file:
    # print(f)
    val = f.stem.split("-")
    print(val)

    # val = val[1].split(".")
    # print(val)
    # print(f.stem)
    # print(f.stat().st_size)
    # print(f.stat().st_mtime)
    # print(f.suffix)
    # print(f.read_text())

# print(list(data_path.glob("a*.*")))

# f_path = Path(r"C:\Users\ramna\OneDrive\Desktop\Navratri Event")
# print(f_path)
# for f in f_path.rglob("*"):
#     print(f.stem)
