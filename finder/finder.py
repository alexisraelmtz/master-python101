from pathlib import Path
import re


def Finder(input):
    filename = Path()
    z = set()
    find = (input) + ".txt"
    for filename in filename.glob("*.txt"):
        iteration = str(filename)
        if find == iteration:
            with open(filename, "r") as f:
                string = str(filename)
                x = string[0:10]
                text = f.readline()
                mo = re.search(r"\d{14}", text)
                y = mo.group()
                z.add((x, y))
    return z


status = False
while not status:
    id = input("Provide a Serial Number... > ").strip()
    if id.lower() == "exit":
        break
    elif not re.match(r"\D{2}\d{5}\w{3}", id) or len(id) > 10:
        print("Please Provide a Valid Seral Number...")
    else:
        print("Searching...")
        result = Finder(id)
        for value in result:
            print(f"\nSerial: {value[0]} \nCOA: {value[1]}")
        again = input("\nTo make a New Query type Any Key or Exit to Leave. ").strip()
        if again.lower() == "exit":
            print("Goodbye.")
            status = True
