import time

count = "Pepperoni"


def f():
    count = "Hawaii"
    print(count)


print("And the best pizza is...")
time.sleep(1)
f()
