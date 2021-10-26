# crypt = ["TEN", "TWO", "ONE"]

# solution = [['O', '1'],
#             ['T', '0'],
#             ['W', '9'],
#             ['E', '5'],
#             ['N', '4']]

# crypt = ["SEND",
#          "MORE",
#          "MONEY"]
# solution = [["O", "0"],
#             ["M", "1"],
#             ["Y", "2"],
#             ["E", "5"],
#             ["N", "6"],
#             ["D", "7"],
#             ["R", "8"],
#             ["S", "9"]]

crypt = ["WASD",
         "IJKL",
         "AOPAS"]
solution = [["W", "2"],
            ["A", "0"],
            ["S", "4"],
            ["D", "1"],
            ["I", "5"],
            ["J", "8"],
            ["K", "6"],
            ["L", "3"],
            ["O", "7"],
            ["P", "9"]]


def isCryptSolution(crypt=crypt, solution=solution):
    hasher = {}
    for list in solution:
        if not list[0] in hasher:
            hasher[list[0]] = (list[1])

    validate = []
    for word in crypt:
        converted = ""
        for letter in word:
            converted += hasher[letter]
        validate.append((converted))

    if validate[0][0:1:1] != '0' or (validate[0]) == '0':
        if validate[1][0:1:1] != '0' or (validate[1]) == '0':
            if validate[2][0:1:1] != '0' or (validate[2]) == '0':
                if int(validate[0]) + int(validate[1]) == int(validate[2]):
                    return True
    return False


result = isCryptSolution()
print(result)
