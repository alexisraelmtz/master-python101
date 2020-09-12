import re
from pathlib import Path


def sku_finder(input):
    filename = Path()
    data = set()
    find = (input) + ".txt"
    for filename in filename.glob("*.txt"):
        iteration = str(filename)
        if find == iteration:
            with open(filename, "r") as f:
                serial = (str(filename))[0:10]
                text = f.readline()
                match = re.search(r"\d{14}", text)
                sku = match.group()
                output = (serial, sku)
                data.add(output)
    return data


def serial_finder(input2):
    filename = Path()
    data = set()
    for filename in filename.glob("*.txt"):
        serial = (str(filename))[0:10]
        with open(filename, "r") as f:
            content = f.readline()
            match = re.search(r"\d{14}", content)
            sku = match.group()
            output = (serial, input2)
            if sku == input2:
                data.add(output)
    return data


continuar = True
while continuar:
    query = input("Search with SKU or Serial? > ").strip()
    if query.lower() == "exit":
        break
    while continuar:
        if query.lower() != "sku":
            id = input("Provide a Serial Number... > ").strip()
            if id.lower() == "exit":
                continuar = False

            elif not re.match(r"\D{2}\d{5}\w{3}", id) or len(id) > 10:
                print("Please Provide a Valid Serial Number...")
            else:
                print("Searching...")
                result = sku_finder(id)
                for value in result:
                    print(f"\nSerial: {value[0]} \nSKU: {value[1]}")
                break

        else:
            id1 = input("Provide a SKU... > ").strip()
            if id1 == "exit":
                continuar = False
            elif not re.match(r"\d{14}", id1) or len(id1) > 14:
                print("Please Provide a valid SKU...")
            else:
                print("Searching...")
                output = serial_finder(id1)
                for value1 in output:
                    print(f"\nSerial: {value1[0]} \nSKU: {value1[1]}")
                break

    while continuar:
        again = input("\nTo make a New search type Any Key or Exit. ").strip()
        if again.lower() != "exit":
            print("\n")
            break
        else:
            continuar = False


# str("03260354832078")
# TJ20323W33