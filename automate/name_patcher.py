import os

# from pathlib import Path


def patcher(folder):
    print("Fetching files ... \nPlease wait . . .")
    directory = os.path.join("/mnt/c/Users/7K/", folder)
    os.chdir(directory)
    n = 0
    for file in os.listdir():
        f_name, f_ext = os.path.splitext(file)
        title, course, f_class = f_name.split("-")
        _, num = f_class.split()
        num = num[1:]

        new = f"{num:0>2s} - {title.strip()}{f_ext}"

        n += 1

        os.rename(file, new)
    print(f"({n} files Found)")


relative = input("Type relative path of Folder to Patch Name Files:\n ").strip()
# relative = "Documents/Python/master-python101/scramble_names/"
patcher(relative)
