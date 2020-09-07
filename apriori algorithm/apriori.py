def createC1(dataSet):
    C1 = []
    for data in dataSet:
        C1 += data
    C1.sort()
    return list(set(C1))


def createFk(dataSet, Ck, minsup):
    Fk_countSup = {}

    for k in Ck:
        count = 0
        for data in dataSet:
            if set(k).issubset(set(data)):
                count += 1
        Fk_countSup[tuple(k)] = count

    Fk = []
    for itemSet in Fk_countSup.keys():
        if (Fk_countSup[itemSet] >= minsup):
            Fk.append(itemSet)
    return Fk


def generateCk(Fk):
    Ck = []
    for i in range(len(Fk)):
        for j in range(i + 1, len(Fk)):
            item_join = list(set(Fk[i] + Fk[j]))
            if len(item_join) == len(Fk[0]) + 1:
                item_join.sort()
                Ck.append(item_join)
    return Ck


def apriori(dataSet, minsup):
    Ck = createC1(dataSet)
    list_Fk = []
    while True:
        Fk = createFk(dataSet, Ck, minsup)
        if len(Fk) == 0: break
        list_Fk.append(Fk)
        Ck = generateCk(Fk)

    return list_Fk


dataSet = [['A', 'B', 'D', 'E'], ['B', 'C', 'E'], ['A', 'B', 'D', 'E'], ['A', 'B', 'C', 'E'], ['A', 'B', 'C', 'D', 'E'],
           ['B', 'C', 'D']]
minsup = 3
list_Fk = apriori(dataSet, minsup)
for i in range(len(list_Fk)):
    print('F' + str(i + 1), list_Fk[i])




