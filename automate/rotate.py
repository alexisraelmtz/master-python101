a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# b = a.copy()
# print([n for n in range(len(a))])


def rotateImage(a):
    b = [[x[i] for x in a][::-1] for i in range(len(a))]
    return b


rotation = rotateImage(a)
print(rotation)


def rotateImage2(a):
    e = len(a)
    b = [[] for _ in range(e)]
    a.reverse()
    for nest in a:
        for index, pixel in enumerate(nest):
            b[index].append(pixel)
    return b


from collections import deque


def rotateLeft(d, arr):
    a = deque()
    a.extend(arr)
    a.rotate(-d)
    return a


d = 4
z = ("1 2 3 4 5").split()
print(z)
r = rotateLeft(d, z)
print(" ".join(r))