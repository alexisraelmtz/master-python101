# BuzzFizz

# a1 = list(map(int, input().split()))


def Buzz(numbers):
    v4 = []
    f = "Fizz"
    b = "Buzz"
    fb = "FizzBuzz"
    for i in numbers:
        if i % 5 == 0 and i % 3 == 0:
            v4.append(fb)
        elif i % 5 == 0:
            v4.append(b)
        elif i % 3 == 0:
            v4.append(f)
        else:
            v4.append(i)
    return v4


r3 = Buzz(range(1, 101))
# r3 = Buzz(a1)
for n in r3:
    print(n)
