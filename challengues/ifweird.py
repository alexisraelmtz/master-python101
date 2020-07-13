#!/bin/python3

import math
import os
import random
import re
import sys

numbers = []
n = int(input("Enter number of elements : "))
for number in range(n):
    digit = int(input("Input a number>  "))
    numbers.append(digit)

# numbers = (3, 24, 6, 20)
for n in numbers:

    if n <= 1:
        print("Input a number bigger than 1")
        break
    while n <= 100:
        if n % 2 == 0:
            if n in range(6, 21):
                print("Weird")
                break
            else:
                print("Not weird")
                break
        else:
            print("Weird")
            break
    else:
        print("Print a number smaller than 100 and grater and 1")
        break


n = int(input("> ").strip())
var = {True: "Not Weird", False: "Weird"}

print(var[n % 2 == 0 and (n in range(2, 6) or n > 20)])

