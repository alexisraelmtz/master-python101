import random
import copy


def insertion(raw):
    sudoku = [[] for _ in range(9)]
    for x, line in enumerate(raw):
        for number in line:
            n = int(number)
            sudoku[x].append(n)
        print(sudoku[x])
    return sudoku


def isTrue(line):
    verify = set()
    for n in line:
        if n == 0:
            return False
        if n in verify:
            return False
        else:
            verify.add(n)
    return True


def correct(solution):

    # X axis verification:
    for line in solution:
        if not isTrue(line):
            return False

    # Y axis verification:
    for i in range(len(line)):
        if not isTrue([line[i] for line in solution]):
            return False

    # 3x3 box verification:
    for x in range(0, 9, 3):
        for y in range(0, 9, 3):
            if not isTrue(
                solution[x][y : y + 3]
                + solution[x + 1][y : y + 3]
                + solution[x + 2][y : y + 3]
            ):
                return False
    return True


############################


def valid(evaluated, existing):
    # line validation in X axis
    # evaluated = set(line)
    new = set()
    # new.update(existing)
    for i, n in enumerate(evaluated):
        if n == 0:
            continue
        if n == existing[i]:
            continue
        # if n in existing and n != existing[i]:
        #     return False
        if n in new:
            return False
        else:
            new.add(n)
    return True


def compare(line):
    existing = [digit for digit in line if digit != 0]
    return existing
    # for digit in line:
    #     if digit != 0:
    #         existing.append(digit)
    # return existing


def generate(exception):
    possible = list(range(1, 10))
    random.shuffle(possible)
    existing = compare(exception)
    for i in existing:
        if i in possible:
            possible.remove(i)
        else:
            continue
    return possible


def calculate(number, exception):
    possible = generate(exception)
    # if numbers[zero] != exception[zero]:
    # number.insert(0, random.choice(possible))
    number = random.choice(possible)
    return number


# def unique(numbers, unsolved):
#     solution = set()
#     unedit = copy.deepcopy(unsolved)
#     for i, n in enumerate(numbers):
#         # existing = compare(unsolved)
#         if n == 0:
#             calculate(numbers, i, unedit)
#         elif n != 0 and n == unedit[i]:
#             continue
#         elif n in unedit:
#             calculate(numbers, i, unedit)
#         elif n in solution:
#             calculate(numbers, i, unedit)
#         else:
#             solution.add(n)
#         #     # calculate(numbers, i, existing)
#     return numbers


############################


def solve(grid):
    start = copy.deepcopy(grid)
    # while True:
    # X axis verification:
    for i, line in enumerate(grid):
        existing = start[i]
        solution = set()
        for x in range(len(grid)):
            n = existing[x]
            if n == 0:
                calculate(n, existing)
                while not real(grid):
                    calculate(n, existing)
                continue
            elif n != 0 and n == existing[i]:
                continue
            elif n in existing:
                calculate(n, existing)
            elif n in solution:
                calculate(n, existing)
            else:
                solution.add(n)

    #         y_axis = [row[x] for row in grid]
    #         y_existing = [vertical[x] for vertical in start]
    #         new_line = unique(line, existing)
    #         # if existing[x] == 0:
    #         while existing[x] == 0:
    #             new_line = unique(line, existing)

    #         grid.remove(grid[i])
    #         grid.insert(i, new_line)

    #         for z in range(0, 9, 3):
    #             for y in range(0, 9, 3):
    #                 cubes = (
    #                     grid[z][y : y + 3]
    #                     + grid[z + 1][y : y + 3]
    #                     + grid[z + 2][y : y + 3]
    #                 )

    # #         # Y axis verification:grid[0]
    # #         for x in range(len(grid)):
    # #             y_axis = [row[x] for row in grid]
    # #             y_existing = [vertical[x] for vertical in start]
    # #             if not valid(y_axis, y_existing):
    # #                 new_axis = unique(y_axis, y_existing)
    # #                 while not valid(new_axis, y_existing):
    # #                     new_axis = unique(y_axis, y_existing)
    # #                 for z in range(9):
    # #                     grid[x].remove(grid[x][z])
    # #                     grid[x].insert(z, new_axis[z])
    # #                     # grid[x][z].append(new_line[z])

    # #

    # #                 # # 3x3 box verification:
    # #                 # for x in range(0, 9, 3):
    # #                 #     for y in range(0, 9, 3):
    # #                 #         cubes = grid[x][y : y + 3] + grid[x + 1][y : y + 3] + grid[x + 2][y : y + 3]
    # #                 #         ):
    # #                 #         if not valid(cubes):
    # #                 #             # Generate

    if correct(grid):
        return grid
    else:
        grid.append(["Its", "Wrong"])
        return grid


def real(grid):
    def validator(numbers):
        # ignores 0s in input for RAW data, as long no repeted nums are spotted.
        inside = set()
        for n in numbers:
            if n == 0:
                continue
            if n in inside:
                return False
            else:
                inside.add(n)
        return True

    # X axis verification:
    for line in grid:
        if not validator(line):
            return False

    # Y axis verification:
    for i in range(len(line)):
        if not validator([line[i] for line in grid]):
            return False

    # 3x3 box verification:
    for x in range(0, 9, 3):
        for y in range(0, 9, 3):
            if not validator(
                grid[x][y : y + 3] + grid[x + 1][y : y + 3] + grid[x + 2][y : y + 3]
            ):
                return False
    return True


# input_1 = input().split()
test = (
    "000260701 680070090 190004500 820100040 004602900 050003028 009300074 040050036 703018000"
).split()

# solution = (
#     "435269781 682571493 197834562 826195347 374682915 951743628 519326874 248957136 763418259"
# ).split()

sudoku = insertion(test)
if real(sudoku):
    print("Valid Sudoku")
    grid = solve(sudoku)
    for i, line in enumerate(grid, start=1):
        print(i, line)

else:
    print("Invalid Sudoku")
