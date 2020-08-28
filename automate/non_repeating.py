from collections import Counter

s = "abacacbasd"
# s = "abacabaabacaba"


# def firstNotRepeatingCharacter2(s):
# c = Counter(s)
# print(c)
# for letter in s:
#     if c[letter] == 1:
#         return letter
# return "_"

# def firstNotRepeatingCharacter1(s):
# set_unrep = set(s)
# list_complete = list(s)
# list_mod = list_complete.copy()
# void = "_"
# #
# for num in set_unrep:
#     if num in list_complete:
#         list_mod.remove(num)
# non_reps = set_unrep.difference(list_mod)
# # print(non_reps)
# for i in list_complete:
#     for unique in non_reps:
#         if unique in i:
#             return i
# return void


def firstNotRepeatingCharacter3(s):
    for letter in s:
        if s.index(letter) == s.rindex(letter):
            return letter
    return "_"


result = firstNotRepeatingCharacter3(s)
print(result)
