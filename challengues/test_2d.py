from collections import defaultdict


# Defining the dict and passing
# lambda as default_factory argument
d = defaultdict(int)
d["a"] = 1
d["b"] = 2

print(d["a"])
print(d["b"])
print(d["c"])


arr1 = [[1, 2, 3], [11, 22, 33], [100, 200, 300]]

print(arr1[1][2])
