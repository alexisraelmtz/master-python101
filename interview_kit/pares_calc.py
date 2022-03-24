# from collections import contadorPareser
# from curses import pair_content


# cajon = [1, 1, 2, 3, 4, 5, 6, 6, 6, 4, 2, 3, 1, 1, 2, 3, 6, 8]
cajon = [1, 2, 1, 2, 1, 3, 2]


def paresCalc(cajon):
    contador = 0
    listaColoresUnicos = set(cajon)
    print(listaColoresUnicos)
    while cajon:
        cajon.sort()
        for color in listaColoresUnicos:
            calcetines = cajon.count(color)
            pares, residuo = divmod(calcetines, 2)
            contador += pares
        return contador
    return 0


print(paresCalc(cajon))


def sockMerchant(n, cajonCompleto):
    while n == len(cajonCompleto):
        lista_colores_Unicos = set()
        lista_colores_Unicos.update(cajonCompleto)
        #
        # lista_colores_Unicos = set(cajonCompleto)
        #
        # print(cajonCompleto)
        contadorPares = 0
        for colorUnico in lista_colores_Unicos:
            # color unico#1 -> 1
            #  color unico #2 -> 2
            while cajonCompleto.count(colorUnico) >= 2:
                cajonCompleto.remove(colorUnico)
                cajonCompleto.remove(colorUnico)
                contadorPares += 1
                # calcetines += 2
                # calcetines / 2 = pares#
                # contadorPares = contadorPares + 1
                # x = 9
                # x = x + 1
                # x = (9) + 1
                # x = 10
                # x = 10
                # x = x + 10
                # x += 10837477577575
        return contadorPares
    return -1
