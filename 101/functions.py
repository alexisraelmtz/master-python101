print("Hello World, ")

num1 = float(input("Cubic Calculator. Please Type de Number you want to power:  "))
num2 = float(input("Please Type de Power to Elevate:  "))
phrase = ""
run = False


def fun_cube(num1, num2):
    global run
    run = True
    return pow(float(num1), float(num2))


print("Your Result is equal to: " + str(fun_cube(num1, num2)))

while run == True:

    phrase = str(input("Do you want to use the Cubic Calculator again? "))
    if phrase.lower() in "yes":
        print("YES was detected. Calculate your numerals.")
        num3 = float(input("Please Type de Number you want to power:  "))
        num4 = float(input("Please Type de Power to Elevate:  "))
        fun_cube(num3, num4)
        print("Your Result is equal to: " + str(fun_cube(num3, num4)))
        run = True
    elif phrase.lower() in "no":
        print("NO was detected. Bye bye.")
        run = False
    else:
        print("Invalid operation. Type Yes or No answer: ")
        run = True
