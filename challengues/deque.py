from collections import deque

input1 = list(map(int, input().strip().split()))
print(input1)
input2 = list(map(int, input().strip().split()))
print(input2)


def deque_rotator():
    width = input1[0]
    rotations = input1[1]
    print(f"Number of rotations is:  {rotations}, and the Deque width is: {width}")
    d = deque(input2, maxlen=width)
    d.rotate(-rotations)
    # print(d)
    print(*d, sep=" ")
    return d


print(deque_rotator())
