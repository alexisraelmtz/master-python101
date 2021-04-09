# JSON: { products : [levels aka. "categories before we reach the end Product"] }

#    p1       p2
#   /  \       |
#  C1  C2      L1

# inventory = {"id"=level.head,... "id0983":level.head}


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return self.value


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(value=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(value=elem)
                node = node.next

    def __iter__(self):
        node = self.head
        while node is not None:
            yield (node)
            node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.value)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


def _levelsHelper(nested):
    if nested:
        dic_Count = {}
        dic_Values = {}
        for product in nested:
            id = nested[product]
            arrValues = []
            count = 1
            arrValues.append(product)
            while id:
                if id.next:
                    arrValues.append(id.value)
                    count += 1
                    id = id.next
                else:
                    break
            dic_Count[id.value] = f"{count} Level/s deep."
            dic_Values[id.value] = arrValues
        return dic_Count, dic_Values
    else:
        return False


id1 = "Beauty"
root1 = Node("Makeup")
nodeA = Node("Face")
nodeB = Node("Lipstick")

root1.next = nodeA
nodeA.next = nodeB

id2 = "Cleaning"
root2 = Node("Clothing")
nodeC = Node("Detergent")

root2.next = nodeC

id3 = "Tools"
root3 = Node("Wire Pliers")


inventory = {
    id1: root1,
    id2: root2,
    id3: root3,
}


print(f"{inventory}\n")
# print(root1.value)
# print(root1.next)
count, vals = _levelsHelper(inventory)
print(f"{count}\n{vals}")