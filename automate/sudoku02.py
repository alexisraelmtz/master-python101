# import random
# import copy


def insertion(raw):
    sudoku = [[] for _ in range(9)]
    for x, line in enumerate(raw):
        for number in line:
            n = int(number)
            sudoku[x].append(n)
        print(sudoku[x])
    return sudoku


def correct(solution):
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


def real(grid):
    def validator(numbers):
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


############################


def solve(grid):
    ref = len(grid)
    possible = list(range(1, 10))
    if correct(grid):
        grid.append(["RIGHT."])
        return True

    for x in range(ref):
        for z in range(ref):
            if grid[x][z] == 0:
                for i in possible:
                    grid[x][z] = i
                    if real(grid):
                        grid[x][z] = i
                        if solve(grid):
                            return grid
                    grid[x][z] = 0
                return False

    # grid.append(["Wrong"])
    # if real(grid):
    #     w = 0
    #     for line in grid:
    #         w += line.count(0)
    #     grid.append(["None", "Repeating", w])
    #     return grid
    # else:
    #     grid.append(["Repeating"])
    #     return grid


############################


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
    for i, line in enumerate(grid, start=0):
        print(i, line)
else:
    print("Invalid Sudoku")
