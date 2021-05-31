repetidos = [5, 9, 7, 5, 9, 4, 2, 3, 1, 5, 9, 7, 3, 7, 6, 3, 5, 1]
unicos = []

base_datos = {
    1: "Uno",
    2: "Dos",
    3: "Tres",
    4: "Cuatro",
    5: "Cinco",
    6: "Seis",
    7: "Siete",
    8: "Ocho",
    9: "Nueve",
    0: "Cero",
}


for number in repetidos:
    if number not in unicos:
        unicos.append(number)
        max = unicos[0]
        for numero in unicos:
            if numero > max:
                max = numero

print(base_datos.get(max, "Did not found key"))
