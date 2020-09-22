def insertion(raw):
    sudoku = [[] for _ in range(9)]
    for x, line in enumerate(raw):
        for number in line:
            sudoku[x].append(number)
        # print(sudoku[x])
    return sudoku


def generate(digit):
    possible = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in possible:
        return i


def unique(numbers):
    solution = set()
    for n in numbers:
        if n == 0:
            continue

        if n in solution:
            return False
        else:
            solution.add(n)
    return True


def verify(grid):
    # X axis verification:
    for line in grid:
        if not unique(line):
            return False
            # Generate

    # Y axis verification:
    for i in range(len(line)):
        if not unique([line[i] for line in grid]):
            return False
            # Generate

    # 3x3 box verification:
    for x in range(0, 9, 3):
        for y in range(0, 9, 3):
            if not unique(
                grid[x][y : y + 3], grid[x + 1][y : y + 3], grid[x + 2][y : y + 3]
            ):
                return False
                # Generate
    return True


# input_1 = input().split()
test = (
    "123456987 000000000 111111111 222222222 333333333 888888888 999999999 123456987 000000000"
).split()


# mk1 = insertion(test)
# print(mk1)
su = insertion(test)
isGrid = verify(su)
print(isGrid)