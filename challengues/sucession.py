n = int(input())

# using for loop = more lines of code

for i in range(1, n + 1):
    print(i, end="")

print("\n")

# diferent method using * :
# single star * unpacks the sequence/collection into positional arguments
# DRY: Dont repeat yourself


n = int(input("> "))
print(*range(1, n + 1), sep="")

