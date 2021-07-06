import sys

# import numpy
# import pandas

# print(sys.version)
# print(sys.executable)


def hi(who_is):
    hello = f"Hello {who_is}"
    print(sys.version)
    print(sys.executable)
    return hello


var = hi("Shaddai")
print(f"{var}, \nSuccessful test!")
