import math


def diagonalDifference(arr):
    a = int(len(arr))
    arr1 = []
    arr2 = []
    for i in range(a):
        arr1.append(arr[i][i])
        arr2.append(arr[i][(a - 1) - i])
    print(arr1)
    print(arr2)
    res = (sum(arr1) - sum(arr2)) ** 2
    # print(res1)
    res1 = int(math.sqrt(res))
    return res1


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
