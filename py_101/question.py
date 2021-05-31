import random

for i in range(3):
    print(random.randint(0, 10))

users = ["A", "B", "C", "D", "E"]
winner = random.choices(users)
print(winner)
