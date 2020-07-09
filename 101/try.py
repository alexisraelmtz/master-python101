try:
    age = int(input("Age: "))
    value = 1
    risk = value / age
    print(age)
except ValueError:
    print("Incorrect Value not Integrer")
except ZeroDivisionError:
    print("Age can not be 0")
