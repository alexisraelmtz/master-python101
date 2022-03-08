def liveSuggestion(database, input):
    if input:
        input = input.lower()
        print(f'{input}')
        print(database)
        database = list(sorted(database))
        output = []
        for index in range(len(input)+1):
            tempList = []
            if index >= 2:
                tempWord = input[0:index]
                # limit = 0
                for word in database:
                    if len(tempList) >= 3:
                        break
                    if word.lower().startswith(tempWord):
                        tempList.append(word)
                    else:
                        tempList += []
                output.append(tempList)
        # print(f'{output}')
        return output


database = ["bags",
            "baggage",
            "banner",
            "box",
            "cloths"]
input = "bags"
print(liveSuggestion(database, input))
