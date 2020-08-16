answer = list(
    map(
        int, input("Place a number to start, and the lenght of the succesion: ").split()
    )
)
start = answer[0]
length = answer[1]


def Fibo(start, length):
    succesion = []
    if start == 0:
        a, b = (start), (1)
    elif start <= 1:
        a, b = (start - 1), (start)

    for _ in range(length):
        succesion.append(a)
        a, b = b, a + b
    return succesion


succesion = Fibo(start, length)
print(succesion)


# start = 1
# length = 10

# a, b = (start - 1), (start)
# for _ in range(length):
#     print(f"{a}")
#     a, b = b, a + b
