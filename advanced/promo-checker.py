def patternCheck(codeList, shoppingCart):
    sizeCart = len(shoppingCart)
    sizeList = len(codeList)
    for index in range(sizeCart):
        if shoppingCart[index] in codeList[0]:
            for n in range(index-1):
                if shoppingCart[n] == codeList[n]:
                    continue
                return 0
            return 1
        continue


"""
4
orange
apple apple
banana orange apple
banana
7
orange
apple
apple
banana
orange
apple
banana
=
1
---
3
apple apricot
banana anything guava
papaya anything
7
banana
orange
guava
apple
apricot
papaya
kiwi
=
0
"""
