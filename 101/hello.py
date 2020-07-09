print("Hello World")

num1 = input("Cubic Calculator. Please Type de Number you want to power:  ")
num2 = input("Please Type de Power to Multiply:  ")


def fun_cube(num1, num2):
    return pow(int(num1), int(num2))


result = fun_cube(num1, num2)
print("Your Result is equal to: " + str(result))
