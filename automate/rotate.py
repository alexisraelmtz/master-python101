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
