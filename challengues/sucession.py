n = int(input())


for i in range(1, n + 1):
    print(i, end="")

print("\n")

n = int(input("> "))
print(*range(1, n + 1), sep="")

