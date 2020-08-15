# a = [2, 4, 3, 5, 1]
a = [4, 3, 3, 1, 5, 2]
# a = [3, 3, 2, 2, 4, 6, 5]
# print(len(a) - 1)

# If you do want to solve it within the memory limit, the restrictions on the values a[i] are critical in this
# problem. Changing the array in place doesn't require extra memory.


def firstDuplicate(a):
    dic = {}
    for index, number in enumerate(a):
        if a.index(number) not in dic:
            dic[index] = a.index(a[index])
        else:  # a.index(number) in dic:
            return a[index]
    return -1


# my_set = {1,2,3,4,5,}
def firstDuplicate2(a):
    l = len(a)
    ab = [0] * (l + 1)
    for i in range(l):
        if ab[a[i]] == -1:
            return a[i]
        else:
            ab[a[i]] = -1
            return -1


result = firstDuplicate(a)
print(result)

