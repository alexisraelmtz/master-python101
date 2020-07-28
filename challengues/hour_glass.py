# print(input1)
# print(input1[0:3])

arr = [
    [-9, -9, -9, 1, 1, 1],
    [0, -9, 0, 4, 3, 2],
    [-9, -9, -9, 1, 2, 3],
    [0, 0, 8, 6, 6, 0],
    [0, 0, 0, -2, 0, 0],
    [0, 0, 1, 2, 4, 0],
]


# for _ in range(6):
#    arr.append(list(map(int, input().split())))
# for row in range(6):
#    print(arr[row])
max1 = []
max2 = []
for x in range(4):
    arrx = []
    arrx.append(
        arr[0][0 + x]
        + arr[0][1 + x]
        + arr[0][2 + x]
        + arr[1][1 + x]
        + arr[2][0 + x]
        + arr[2][1 + x]
        + arr[2][2 + x]
    )
    #
    max1.append(arrx)

    for y in range(3):
        arry = []
        arry.append(
            arr[1 + y][0 + x]
            + arr[1 + y][1 + x]
            + arr[1 + y][2 + x]
            + arr[2 + y][1 + x]
            + arr[3 + y][0 + x]
            + arr[3 + y][1 + x]
            + arr[3 + y][2 + x]
        )
        #
        max2.append(arry)


max1.extend(max2)
print(max1)
print(f"Length: {len(max1)}")
# max1.sort()
total = []

for i in range(16):

    total.append(sum(max1[i]))

total.sort()
print(total)

print(f"Max sum value: {total[15]}")

# print(f"{max1[0]} {max1[15]}")

