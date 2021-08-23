dishes = [["Salad", "Tomato", "Cucumber", "Salad", "Sauce"],
          ["Pizza", "Tomato", "Sausage", "Sauce", "Dough"],
          ["Quesadilla", "Chicken", "Cheese", "Sauce"],
          ["Sandwich", "Salad", "Bread", "Tomato", "Cheese"]]


# def groupingDishes(dishes):
#     # list[0] = dish
#     # list[1:] = ingredients

#     # check true dishes
#     if dishes:
#         # get all unique ingredients
#         uniqueIngredients = set(
#             [ingredient for foodList in dishes for ingredient in foodList[1::]])
#         # menu = set([dish[0] for dish in dishes])
#         mother = list()
#     # for dish if item in dish
#         for item in uniqueIngredients:
#             # position = list(uniqueIngredients).index(item)
#             temp = set()
#             # for x, _ in enumerate(dishes):
#             for n in range(len(dishes)):
#                 if item in dishes[n]:
#                     # check more than 2 dishes condition
#                     temp.add(dishes[n][0])
#                     # add dish to set
#             tempTwo = (list(temp))
#             if len(tempTwo) >= 2:
#                 tempTwo.sort()
#                 tempTwo.insert(0, item)
#                 mother.append(tempTwo)
#             mother.sort()
#             # print(list(temp))
#             # tempTwo.insert(0, i)
#             # mother.append(tempTwo)
#             # mother.append(list(temp))
#     return mother
#     # make list(set)
#     # append list to mother
#     # return mother


def groupingDishesOld(dishes):
    if dishes:
        uniqueIngredients = set(
            [ingredient for foodList in dishes for ingredient in foodList[1::]])
        mother = list()
        for item in uniqueIngredients:
            temp = list()
            for n in range(len(dishes)):
                if item in dishes[n]:
                    temp.append(dishes[n][0])
            if len(temp) >= 2:
                temp.sort()
                temp.insert(0, item)
                mother.append(temp)
        mother.sort()
    return mother


def groupingDishes(dishes):
    if dishes:
        myCollection = {}
        for key, *values in dishes:
            for item in values:
                myCollection.setdefault(item, []).append(key)
        mother = list()
        for n in sorted(myCollection):
            if len(myCollection[n]) >= 2:
                mother.append([n]+sorted(myCollection[n]))
    return mother  # [ingredient name, ... dishes...]


print(groupingDishes(dishes))


# def groupingDishes(dishes):
#     groups = {}
#     for d, *v in dishes:
#         for x in v:
#             groups.setdefault(x, []).append(d)
#     ans = []
#     for x in sorted(groups):
#         if len(groups[x]) >= 2:
#             ans.append([x] + sorted(groups[x]))
#     return ans
