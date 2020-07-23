alice = []
bob = []

# Triplets(): Iterates until numbers/scores are integrated into diferent integrer arrays.
# e.g. Bob and Alice. Each with 3 scores.


def triplets():

    n = 1

    while n < 3:
        s = input().split()
        # print(s)
        if n == 1:
            for i in range(3):
                alice.append(int(s[i]))
            # print(alice)
        elif n == 2:
            for i in range(3):
                bob.append(int(s[i]))
            # print(bob)
        n += 1

    return (alice, bob)


def compare(a, b):
    r = []
    al_r = 0
    bo_r = 0

    if a[0] > b[0]:
        al_r += 1
    elif a[0] == b[0]:
        pass
    else:
        bo_r += 1

    if a[1] > b[1]:
        al_r += 1
    elif a[1] == b[1]:
        pass
    else:
        bo_r += 1

    if a[2] > b[2]:
        al_r += 1
    elif a[2] == b[2]:
        pass
    else:
        bo_r += 1

    # r.append(al_r)
    # r.append(bo_r)
    print(f"{al_r} {bo_r}")

    return (al_r, bo_r, r)


triplets()
compare(alice, bob)

