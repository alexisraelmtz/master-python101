
try:

    i = 1

    while i == 1:
        phrase = str(input("Do you want to Calculate again? "))
        if phrase.lower() in "yes":
            print("YES was detected")
            i -= 1
        elif phrase.lower() in "no":
            print("NO was detected, bye bye.")
            i -= 1
        else:
            print("Invalid operation. Type Yes or No answer. ")
            i += 0

except:
    print("Valio Versh")

"""
try:
    phrase = "Thank you for using, "
    print(phrase)
    while phrase.lower() != "yes" or "no":
        phrase = str(input("Do you want to Calculate again? "))
        if phrase.lower() == "yes":
            print("YES was detected")
            phrase == "no"
        elif phrase.lower() == "no":
            print("NO was detected, bye bye.")
            phrase == "no"
        else:
            print("Invalid operation. Type Yes or No answer. ")
            phrase != "yes" and "no"


except:
    print("Valio Versh")
"""