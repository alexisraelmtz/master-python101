input1 = list(map(int, input().strip().split()))
print(input1)


def min_max():
    n = (len(input1)) - 1
    array = []
    for element in input1:
        net = (sum(input1)) - element
        array.append(net)
    array.sort()
    print(array)
    print(f"{array[0]} {array[n]}")


min_max()
