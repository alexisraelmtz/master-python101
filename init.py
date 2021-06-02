import sys

# import pandas

# print(sys.version)
# print(sys.executable)


def hi(who_is):
    hello = f"Hello {who_is}"
    print(sys.version)
    print(sys.executable)
    return hello


print(hi("Alex"))
var = hi("Shaddai")
print(f"{var}, \nSuccessful test!")
