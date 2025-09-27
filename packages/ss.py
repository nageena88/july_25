from pathlib import Path

path = Path(".")
# print(path.absolute())
data_path = path.joinpath("packages", "data")
jan_files = data_path.glob("*jan*")
for file in jan_files:
    print(file.name)
    print(file.stem.split("_")[-1])
    if file.stem.split("_")[-1] == "1":
        print("First file")
