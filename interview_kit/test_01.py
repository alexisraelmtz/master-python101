import re


def validate(username):
    if username:
        chars = int(len(username))
        if chars >= 4:
            match = re.search(r"[_]?[a-zA-Z0-9]*[^_]$", username)
            match_01 = re.search(r"[a-zA-Z0-9]*[_]?[a-zA-Z0-9]*[^_]$", username)
            if match or match_01:
                if match.group() == username or match_01.group() == username:
                    return True
    return False


n = validate("_MikeStandish99")
print(f"Valid name: {n}")  # Valid username
n = validate("Mike__Standish0")
print(f"Valid name: {n}")  # Invalid username


def john_mary(string):
    if string and type(string) == str:
        a1 = string.upper().split("&")
        if "JOHN" in a1 and "MARY" in a1:
            z = a1.count("JOHN")
            x = a1.count("MARY")
            if z == x:
                return True
    return False


n = "John&Mary&Mary"
print(f"John and Mary are in pairs: {john_mary(n)}")


import string


def numbers_to_letters(s):
    hash = {}
    for z, i in enumerate(range(65, 91), start=1):
        hash[z] = chr(i)

    num_words = s.split("+")
    arr = []

    for i in range(len(num_words)):
        num = num_words[i].split()
        newWord = ""
        for j in num:
            char = hash.get(int(j))
            newWord += str(char)
        arr.append(newWord)
    return " ".join(arr)


if __name__ == "__main__":
    print(numbers_to_letters("20 5 19 20+4 15 13 5+20 5 19 20"))


def minimal_number_of_packages(items, large, small):
    fit_large = items // 5  # 1 round
    fit_small = items % 5  # 4 reminder

    # print(f"{fit_large}\n{fit_small}")

    l = large * 5
    max = l + small
    if items <= max:
        if fit_large <= large and fit_small <= small:
            return fit_large + fit_small
        elif fit_large > large:
            fit_small = items - (large * 5)
            if fit_small > small:
                return -1
            return large + fit_small
    return -1


print(f"{minimal_number_of_packages(11, 2, 4)} packages where used.")


def group_by_owners(files):
    if files:
        newd = {}
        for key in files:
            if files[key] in newd[key]:
                arr = []
                del newd[key]
                arr.append(files[key])
                arr.append(key)
                newd[files[key]] = arr
            newd[files[key]] = key
    return newd


if __name__ == "__main__":
    files = {"Input.txt": "Randy", "Code.py": "Stan", "Output.txt": "Randy"}
    print(group_by_owners(files))