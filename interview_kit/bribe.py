# from queue import Queue

# 2
# 5
# 2 1 5 3 4
# 5
# 2 5 1 3 4

# a = "1 2 5 3 7 8 6 4"
a = "1 2 5 3 7 8 6 4"
q = list(map(int, a.strip().split()))


# Complete the minimumBribes function below.
def minimumBribes(q):
    over = False
    bribes = 0
    size = len(q)
    arr = [i for i in range(1, size + 1)]
    print(f"{arr}\n{q}")
    for n in range(size):
        person = q[n]  # P
        original = arr[n]  # i
        count = person - original
        if 0 < count > 2:
            return f"Too chaotic"
        for i in range(max(person - 2, 0), original):
            if q[i] > person:
                bribes += 1
    return bribes


res = minimumBribes(q)
print(res)

if __name__ == "__main__":
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
