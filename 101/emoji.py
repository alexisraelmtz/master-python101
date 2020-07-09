def emoji_converter():

    words = text.split(" ")
    emoji = {":)": ">:D", ":(": ":C"}

    output = ""
    for word in words:
        output += emoji.get(word, word) + " "
    return output


text = input("> ")
print(emoji_converter())
