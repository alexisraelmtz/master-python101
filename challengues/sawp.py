def case_converter():

    words = text.split(" ")
    output = ""

    for word in words:
        for letter in word:
            if letter == letter.lower():
                output += letter.upper()
            else:
                output += letter.lower()
        output += " "
    return output


text = input("> ")
print(case_converter())


# Pythonist 2 -> pYTHONIST 2
