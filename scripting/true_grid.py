# grid = [
#     [".", ".", ".", "1", "4", ".", ".", "2", "."],
#     [".", ".", "6", ".", ".", ".", ".", ".", "."],
#     [".", ".", ".", ".", ".", ".", ".", ".", "."],
#     [".", ".", "1", ".", ".", ".", ".", ".", "."],
#     [".", "6", "7", ".", ".", ".", ".", ".", "9"],
#     [".", ".", ".", ".", ".", ".", "8", "1", "."],
#     [".", "3", ".", ".", ".", ".", ".", ".", "6"],
#     [".", ".", ".", ".", ".", "7", ".", ".", "."],
#     [".", ".", ".", "5", ".", ".", ".", "7", "."],
# ]

grid = [
    [".", "4", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", "4", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", "1", ".", ".", "7", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", "3", ".", ".", ".", "6", "."],
    [".", ".", ".", ".", ".", "6", ".", "9", "."],
    [".", ".", ".", ".", "1", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "2", ".", "."],
    [".", ".", ".", "8", ".", ".", ".", ".", "."],
]

# def sudoku2(grid):
#     l = len(grid)
#     vertical = [set() for _ in range(l)]
#     multi = [set() for _ in range(l)]

#     for row in grid:
#         for n in row:
#             if n.isdigit():
#                 if row.count(n) > 1:
#                     return False
#                 elif n in vertical[row.index(n)]:
#                     return False
#                 elif n not in vertical[row.index(n)]:
#                     vertical[row.index(n)].add(n)

#             if n.isdigit():
#                 if row in grid[0:3]:
#                     if row.index(n) in {0, 1, 2} and n not in multi[0]:
#                         multi[0].add(n)
#                     elif row.index(n) in {3, 4, 5} and n not in multi[1]:
#                         multi[1].add(n)
#                     elif row.index(n) in {6, 7, 8} and n not in multi[2]:
#                         multi[2].add(n)
#                     else:
#                         return False
#                 elif row in grid[3:6]:
#                     if row.index(n) in {0, 1, 2} and n not in multi[3]:
#                         multi[3].add(n)
#                     elif row.index(n) in {3, 4, 5} and n not in multi[4]:
#                         multi[4].add(n)
#                     elif row.index(n) in {6, 7, 8} and n not in multi[5]:
#                         multi[5].add(n)
#                     else:
#                         return False
#                 elif row in grid[6:9]:
#                     if row.index(n) in {0, 1, 2} and n not in multi[6]:
#                         multi[6].add(n)
#                     elif row.index(n) in {3, 4, 5} and n not in multi[7]:
#                         multi[7].add(n)
#                     elif row.index(n) in {6, 7, 8} and n not in multi[8]:
#                         multi[8].add(n)
#                     else:
#                         return False
#     return True


def unique(nums):
    s = set()
    for num in nums:
        if num == ".":
            continue

        if num in s:
            return False
        s.add(num)
    return True


def sudoku2(grid):
    for line in grid:
        if not unique(line):
            return False

    for i in range(9):
        if not unique([line[i] for line in grid]):
            return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not unique(
                grid[i][j : j + 3] + grid[i + 1][j : j + 3] + grid[i + 2][j : j + 3]
            ):
                return False

    return True


result = sudoku2(grid)
print(result)