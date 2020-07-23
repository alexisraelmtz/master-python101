n = int(input("Type the number of commands> "))
possibilities = (
    "print",
    "sort",
    "pop",
    "reverse",
    "insert",
    "append",
    "remove",
    "help",
)


def array_application():
    array = []
    for i in range(n):
        text = input("Type the operation> ").split()
        items = int(len(text)) - 1
        command = text[0].strip().lower()
        if command in possibilities:
            if command == "append":
                for i in range(items):
                    array.append(int(text[i + 1]))
                # print(array)
            elif command == "print":
                print(array)
            elif command == "sort":
                array.sort()
            elif command == "pop":
                array.pop()
            elif command == "reverse":
                array.reverse()
            elif command == "insert":
                array.insert(int(text[1]), int(text[2]))
            elif command == "remove":
                array.remove(int(text[1]))
            elif command == "help":
                print(
                    """
            1. insert i e: Insert integer 'e' at position 'i'.
            2. print: Print the list.
            3. remove e: Delete the first occurrence of integer 'e'.
            4. append e: Insert integer 'e' at the end of the list.
            5. sort: Sort the list.
            6. pop: Pop the last element from the list.
            7. reverse: Reverse the list.
                            """
                )
        else:
            print("Command not detected. Type Help for list of commands.")
    return array

    # Missing 1 added loop in case of 'typo' of 'Help' command.


array_application()

