# def rotateImage(img):
#     # backup = img
#     img.reverse()
#     new = [[] for _ in img]
#     for line in img:
#         for pos, pixel in enumerate(line):
#             # pos = img[backup.index(line)].index(pixel)
#             new[pos].append(pixel)
#     return new

def rotateImage(img):
    img.reverse()
    for i in range(len(img)):
        for j in range(i):
            img[i][j], img[j][i] = img[j][i], img[i][j]
    return img


a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

print(rotateImage(a))
