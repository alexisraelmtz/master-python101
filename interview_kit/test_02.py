import numpy as np
# import re


# def validate(username):
#     if username:
#         chars = int(len(username))
#         if chars >= 4:
#             match = re.search(r"[_]?[a-zA-Z0-9]*[^_]$", username)
#             match_01 = re.search(r"[a-zA-Z0-9]*[_]?[a-zA-Z0-9]*[^_]$", username)
#             if match or match_01:
#                 if match.group() == username or match_01.group() == username:
#                     return True
#     return False


# n = validate("_MikeStandish99")
# print(f"Valid name: {n}")  # Valid username
# n = validate("Mike__Standish0")
# print(f"Valid name: {n}")  # Invalid username


# def john_mary(string):
#     if string and type(string) == str:
#         a1 = string.upper().split("&")
#         if "JOHN" in a1 and "MARY" in a1:
#             z = a1.count("JOHN")
#             x = a1.count("MARY")
#             if z == x:
#                 return True
#     return False


# n = "John&Mary&Mary"
# print(f"John and Mary are in pairs: {john_mary(n)}")


# import string


# def numbers_to_letters(s):
#     hash = {}
#     for z, i in enumerate(range(65, 91), start=1):
#         hash[z] = chr(i)

#     num_words = s.split("+")
#     arr = []

#     for i in range(len(num_words)):
#         num = num_words[i].split()
#         newWord = ""
#         for j in num:
#             char = hash.get(int(j))
#             newWord += str(char)
#         arr.append(newWord)
#     return " ".join(arr)


# if __name__ == "__main__":
#     print(numbers_to_letters("20 5 19 20+4 15 13 5+20 5 19 20"))


# def minimal_number_of_packages(items, large, small):
#     capL = large * 5
#     maxCap = capL + small
#     # divimod(x,y) = (x // y , x % y)
#     filled, missing = divmod(items, 5)

#     if items <= maxCap:
#         if filled <= large and missing <= small:
#             count = filled + missing
#         if filled > large:
#             diff = filled - large
#             if diff <= small:
#                 count = (filled - diff) + (items - capL)
#             else:
#                 return -1
#         return count
#     return -1


# print(f"{minimal_number_of_packages(11, 2, 4)} packages where used.")
# print(f"{minimal_number_of_packages(10, 5, 5)} packages where used.")
# print(f"{minimal_number_of_packages(10, 1, 5)} packages where used.")


# def group_by_owners_OLD(files):
#     if files:
#         newd = {}
#         for txt in files:
#             name = files[txt]
#             new = []
#             if name in newd:
#                 old = newd[name]
#                 if isinstance(old, list):
#                     for el in old:
#                         new.append(el)
#                 else:
#                     new.append(old)
#                 new.append(txt)
#                 newd[name] = new
#             else:
#                 new.append(txt)
#                 newd[name] = new
#     return newd


# import numpy as np


def group_by_owners(files):
    if files:
        newd = {}
        for txt in files:
            name = files[txt]
            if name in newd:
                newd[name].append(txt)
            else:
                newd[name] = [txt]
    return newd


if __name__ == "__main__":
    files = {
        "Input.txt": "Randy",
        "Code.py": "Stan",
        "Output.txt": "Randy",
        "Assignment.txt": "Randy",
        "Sleep.txt": "Roy",
        "Angry.txt": "Roy",
    }
    print(group_by_owners(files))


# def unique_names_OLD(names1, names2):
#     def unique(lis):
#         if isinstance(lis, list):
#             for el in lis:
#                 uni.add(el)
#             return uni
#         return uni.add(lis)

#     uni = set()
#     unique(names1)
#     unique(names2)
#     uni = list(uni)
#     return uni


def unique_names(names1, names2):
    return list(set(names1 + names2))


# if __name__ == "__main__":
#     names1 = ["Ava", "Emma", "Olivia"]
#     names2 = ["Olivia", "Sophia", "Emma"]
#     print(unique_names(names1, names2))  # should print Ava, Emma, Olivia, Sophia


# def matchingStrings(strings, queries):
#     found = []
#     for query in queries:
#         count = 0
#         count += strings.count(query)
#         found.append(count)
#     return found


# a = (
#     "abcde sdaklfj asdjf na basdn sdaklfj asdjf na asdjf na basdn sdaklfj asdjf"
# ).split()
# b = ("abcde sdaklfj asdjf na basdn").split()

# print(matchingStrings(a, b))


print("------------------------------------------")


class IceCreamMachine:
    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings

    def scoops(self):
        combs = []
        for ing in self.ingredients:
            for top in self.toppings:
                combs.append([ing, top])
        return combs


machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
print(
    machine.scoops()
)  # should print[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]


# import numpy as np


# def find_roots(a, b, c):
#     coeff = [a, b, c]
#     return tuple(np.roots(coeff))


# print(find_roots(2, 10, 8))


def is_palindrome(word):
    if not word is None:
        word = word.lower()
        return word == word[::-1]
    else:
        return False


print(is_palindrome("Deleveled"))


cars = {
    "Xterra": "Nissan",
    "Odyssey": "Honda",
    "Camaro": "Chevrolet",
    "Aventador": "Lamborghini",
}
for key in cars:
    print(cars[key])


def find_roots(a, b, c):
    vars = [a, b, c]
    return list(np.roots(vars))


print(find_roots(2, 10, 8))

# SELECT
# 	items.name, sellers.name
# FROM
# 	items
# INNER JOIN sellers ON items.sellerId = sellers.id
# WHERE sellers.rating > 4;

# SELECT
# 	userid, AVG(duration)
# FROM
# 	sessions
# GROUP BY 1
# HAVING COUNT (userId) > 1;

# SELECT
# 	dogs.name
# FROM
# 	dogs
# LEFT JOIN cats ON B.n = A.n;


# SELECT name
# FROM dogs
# UNION
# SELECT name
# from cats;

# SELECT name
# FROM employees
# WHERE id not in (SELECT managerId FROM employees WHERE managerId not null);


# SELECT width*height AS Area, count() FROM rectangles
# GROUP BY 1


# SELECT name FROM authors
# WHERE name LIKE 'N%'
# AND(books > 30
#     OR age < 30)


# SELECT trim(name) from developers
# WHERE lower(name) LIKE '%john%'


# UPDATE menu
# SET price = price*1.1
# WHERE category in ("Soups", "Salads")


# INSERT INTO retired_employees
# (id, name)
# SELECT id, name FROM employees
# WHERE retired = "Y"
