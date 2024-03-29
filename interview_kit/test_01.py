import string
import re


# inputTest = list(map(int, ((input()).strip().split())))


# def helperFunc(inputTest):
#     return result


# print(helperFunc(inputTest))


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


# def _validateOld(username):
#     if username:
#         chars = int(len(username))
#         if chars >= 4:
#             match = re.search(r"^[a-zA-Z]+[_]?[a-zA-Z0-9]*[a-zA-Z0-9]$", username)
#             match_01 = re.search(r"^[a-zA-Z]*[a-zA-Z0-9]*[_]?[a-zA-Z0-9]$", username)
#             if match or match_01:
#                 if match.group() == username:
#                     return True
#                 if match_01.group() == username:
#                     return True
#                 else:
#                     return False
#             else:
#                 return False
#     else:
#         return False


def validate(name):
    if len(name) < 4:
        return False
    if not bool(re.match(r"^[a-zA-Z0-9_]+$", name)):
        return False
    return (
        name[0].isalpha() and name[-1].isalnum() and len(re.findall(r"[_]", name)) < 2
    )


print(validate("Mike_Standish_"))  # Valid username
print(validate("Mike Standish_"))  # Invalid username


n = validate("_MikeStandish99")
print(f"Valid name: {n}")  # FALSE Valid username
n = validate("MikeStandish0_")
print(f"Valid name: {n}")  # TRUE Invalid username


def _john_maryOld(string):
    if string and type(string) == str:
        a1 = string.upper().split("&")
        if "JOHN" in a1 and "MARY" in a1:
            z = a1.count("JOHN")
            x = a1.count("MARY")
            if z == x:
                return True
    return False


def john_mary(str):
    return len(re.findall("John", str, re.IGNORECASE)) == len(
        re.findall("Mary", str, re.IGNORECASE)
    )


print(john_mary("John&Mary"))


# n = "John&Mary&Mary"
# print(f"John and Mary are in pairs: {john_mary(n)}")


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
    capL = large * 5
    maxCap = capL + small
    # divimod(x,y) = (x // y , x % y)
    filled, missing = divmod(items, 5)

    if items <= maxCap:
        if filled <= large and missing <= small:
            count = filled + missing
        if filled > large:
            diff = filled - large
            if diff <= small:
                count = (filled - diff) + (items - capL)
            else:
                return -1
        return count
    return -1


print(f"{minimal_number_of_packages(16, 2, 10)} packages where used.")
# print(f"{minimal_number_of_packages(10, 5, 5)} packages where used.")
# print(f"{minimal_number_of_packages(10, 1, 5)} packages where used.")


def group_by_owners_OLD(files):
    if files:
        newd = {}
        for txt in files:
            name = files[txt]
            new = []
            if name in newd:
                old = newd[name]
                if isinstance(old, list):
                    for el in old:
                        new.append(el)
                else:
                    new.append(old)
                new.append(txt)
                newd[name] = new
            else:
                new.append(txt)
                newd[name] = new
    return newd


# def group_by_owners(files):
#     if files:
#         newd = {}
#         for txt in files:
#             name = files[txt]
#             # new = []
#             if name in newd:
#                 newd[name].append(txt)
#             else:
#                 newd[name] = [txt]
#     return newd


# if __name__ == "__main__":
#     files = {
#         "Input.txt": "Randy",
#         "Code.py": "Stan",
#         "Output.txt": "Randy",
#         "Assignment.txt": "Randy",
#         "Sleep.txt": "Roy",
#         "Angry.txt": "Roy",
#     }
#     print(group_by_owners(files))


# def unique_names_OLD(names1, names2):
#     def unique(lis):
#         uni = set()
#         if isinstance(lis, list):
#             for el in lis:
#                 uni.add(el)
#             return uni
#         return uni.add(lis)

#     unique(names1)
#     unique(names2)
#     # # uni = list(uni)
#     # return list(uni)


# def unique_names(names1, names2):
#     return list(set(names1 + names2))


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


# print("------------------------------------------")


# class IceCreamMachine:
#     def __init__(self, ingredients, toppings):
#         self.ingredients = ingredients
#         self.toppings = toppings

#     def scoops(self):
#         combs = []
#         for ing in self.ingredients:
#             for top in self.toppings:
#                 combs.append([ing, top])
#         return combs


# machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
# print(
#     machine.scoops()
# )  # should print[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]


# import numpy as np


# def find_roots(a, b, c):
#     coeff = [a, b, c]
#     return tuple(np.roots(coeff))


# print(find_roots(2, 10, 8))


# def is_palindrome(word):
#     if not word is None:
#         word = word.lower()
#         return word == word[::-1]
#     else:
#         return False


# print(is_palindrome("Deleveled"))

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


def _div(a, b):
    # float("inf")
    # if b != 0:
    try:
        return a / b
    except:
        return "Try different than 0"


# div(0,10) = 0
# div(10,0) = "Try different than 0"

print(_div(0, 10))
print(_div(10, 0))


# atoi("10") = 10 -  C

# "786"


def string_to_int(string):
    def char_to_int(char):
        while char:
            dicChars_Nums = {
                "0": 0,
                "1": 1,
                "2": 2,
                "3": 3,
                "4": 4,
                "5": 5,
                "6": 6,
                "7": 7,
                "8": 8,
                "9": 9,
            }
            try:
                conv = dicChars_Nums[char]
                return conv
            except:
                return False

    a = string
    pos = len(a) - 1  # 3
    sumTo = 0
    for char in string:
        # print(char)
        intNum = char_to_int(char)  # 7
        if intNum:
            intNum = intNum * (1 * (10 ** (pos)))
            # print(intNum)
            pos -= 1
            sumTo += intNum
        else:
            return "Please try Digits (0-9)"
    return sumTo


print(string_to_int("786"))
print(string_to_int("76112"))
print(string_to_int("abc"))
# print(string_to_int("-10"))


# def isBalanced_old(myStr):
#     listOpen = ["(","[","{"]
#     listClose = [")","]","}",]
# 	listLetters = ["a","b",..."z"]
#     myStack = []
#     for item in myStr:
# 		if item in listLetters:
# 			break
#         elif item in listOpen:
#             myStack.append(item)
#         elif item in listClose:
#             position = listClose.index(item)
#             if myStack and (listOpen[position] == myStack[len(myStack)-1]):
#                 myStack.pop()
#             else:
#                 return False
#     if not myStack:
#         return True
#     else:
#         return False


def isBalanced(myStr):
    listOpen = ["(", "[", "{"]
    listClose = [")", "]", "}"]
    myStack = []
    for item in myStr:
        if item in listOpen:
            myStack.append(item)
        else:
            if not myStack:
                return False
            else:
                if item in listClose and myStack.pop() not in listOpen[listClose.index(item)]:
                    return False
    if not myStack:
        return True
    else:
        return False
