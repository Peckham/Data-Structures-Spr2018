def three_way_disjoint(l1, l2, l3):
    ''' Solve disjoint problem using python dictionary. Do not try this way (hw2 solution)!
    lissy = l1 + l2 + l3        # O(n)
    lissy.sort()                # O(nlogn)
    for i in range(len(lissy) - 1):
        if (lissy[i] == lissy[i + 1] == lissy[i + 2]):
            return False

    return True

    '''
    myDict = dict.fromkeys(set([i for i in l1 + l2 + l3]), False)
    for i in myDict.keys():
        if i in l1 and i in l2 and i in l3:
            return False
    return True





l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10, 11, 12]
l3 = [5, 13, 14, 15, 16]
l4 = [5, 6, 7, 8, 9, 10, 11]

# Can't find a number in l1, l2, l3 --> Disjoint
print(three_way_disjoint(l1, l2, l3))
print(three_way_disjoint(l1, l4, l3))  # 5 exist in l1, l3, l4 --> Not disjoint
