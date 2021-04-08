# Complete the Valleys found function below.
def countingValleys(steps, path):
    a = list(path)
    count = 0
    hike = 0
    if len(a) >= 2:
        for step in a:
            if count == 0 and step == "D":
                hike += 1
            if step == "U":
                count += 1
            if step == "D":
                count -= 1
    return hike


steps, path = (8, "UDDDUDUU")
valleys = countingValleys(steps, path)
# Expected 1
#
# 0 __/\      ___ 0
#       \    /
#        \/\/
# A valley is a sequence of consecutive steps below sea level.
print(f"Number of Valleys hiked is {valleys}")


# Complete the sockMerchant function below.
def sockMerchant(n, array):
    while n == len(array):
        set_one = set()
        set_one.update(array)
        # print(array)
        count = 0
        for digit in set_one:
            while array.count(digit) >= 2:
                array.remove(digit)
                array.remove(digit)
                count += 1
        return count
    return -1


# n = int(input())
# array = list(map(int, input().strip().split()))
n = 9
array = list(map(int, ("10 20 20 10 10 30 50 10 20").strip().split()))

pairs = sockMerchant(n, array)
print(f"Pairs of socks found is: {pairs}")


# Sample Input
# 9
# 10 20 20 10 10 30 50 10 20

# Sample Output
# 3


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    while len(c) >= 2:
        jumps = 0
        i = 0
        while i < len(c):
            if c[i] == 0:
                if i + 2 < len(c):
                    if c[i + 2] == 0:
                        jumps += 1
                        i += 2
                        continue
                if i + 1 < len(c):
                    if c[i + 1] == 0:
                        jumps += 1
                        i += 1
                        continue
                return jumps


# 6
# 0 0 0 0 1 0
# Expected: Min = 3. (3 and 4)

clouds = list(
    map(
        int,
        (("0 0 1 0 0 1 0").split()),
    )
)

jumps = jumpingOnClouds(clouds)
print(f"Min. jumps needed is: {jumps}")


# Complete the repeatedString function below.
def repeatedString(s, n):
    size = int(n)
    times, mod = divmod(size, len(s))
    chars = s.count("a")
    if mod == 0:
        new_s = chars * times
        return s, new_s
    new_s = chars * times + s[:mod].count("a")
    return s, new_s


# aba
# 10
# > 7

string, n = list(
    map(
        str,
        (
            (
                "udjlitpopjhipmwgvggazhuzvcmzhulowmveqyktlakdufzcefrxufssqdslyfuiahtzjjdeaxqeiarcjpponoclynbtraaawrps 872514961806"
            )
            .strip()
            .split()
        ),
    )
)
occur = repeatedString(string, n)
print(f"Letter 'a' occurrences found in '{occur[0]}' : {occur[1]:,.2f}")

for _ in range(10):
    print("Hello")