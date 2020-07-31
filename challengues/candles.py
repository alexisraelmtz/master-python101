n = int(input().strip())
arr1 = []
input1 = list(map(int, input().strip().split()))
for i in range(n):
    arr1.append(input1[i])
# print(arr1)


def candles():
    arr1.sort()
    print(arr1.count(arr1[n - 1]))
    return arr1


candles()
