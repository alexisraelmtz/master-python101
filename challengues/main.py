# Python program to execute
# main directly
print("Always executed from main.py")


def my_function():
    if __name__ == "__main__":
        print("Executed when invoked directly")
    else:
        print("Executed when imported as a module.")
