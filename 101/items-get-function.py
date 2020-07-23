from collections import Counter

list1 = [
    1,
    1,
    1,
    1,
    1,
    1,
    9,
    3,
    2,
    5,
    3,
    2,
    69,
    29,
    29,
    0,
    0,
    0,
    0,
    0,
    2,
    3,
    6,
    7,
    4,
    7,
    5,
    7,
]

list_count = Counter(list1)

print(list_count.items())
print(list_count)

print(
    "\nItems func. provides a dictionary that outputs a value for each key(the item). \n1. The Value \n2. The number of times is repeated trought the list."
)
print(
    f"\nThe Value location in index 0. And the number of times is repited in the list, at index 1."
)

for item in list_count.items():
    print(f"So you get that the number {item[0]}, is repeated {item[1]} times.")

print("And finally the value 69 appears {0} times.".format(list_count.get(69)))
