import utils
from utils import find_max


numbers = []
n = int(input("Enter number of elements : "))
for number in range(n):
    digit = int(input())
    numbers.append(digit)

print(numbers)

print(utils.find_max(numbers))


import converters
from converters import kg_2_lbs


print(converters.kg_2_lbs(78))
print(converters.lbs_2_kg(78))

print(kg_2_lbs(int(input("> Type KG to convert to Lbs...  "))))

