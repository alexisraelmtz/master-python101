# Tranductor F


def traductor(phrase):
    traduction = ""
    for letter in phrase:
        try:
            if letter.lower() in "bcdfghjklmnpqrstvwxy":
                if letter.isupper():
                    traduction = traduction + "F" #+ letter(letter.index - 1)
                else:
                    traduction = traduction + "f" #+ letter(letter.index - 1)
            else:
                traduction = traduction +  "fa"
    return(traduction)

print(traductor(input("Enter phrase to converte to F Language: ")))

except TypeError:
    print("Not getting the consonant back")