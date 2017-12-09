def intersect_lists_2(list1, list2):
    for e in list2:
        list1.append(e)
    print(list1)
    s = set(list1)
    print(s)
    return s

intersect_lists_2([1,2,3],[3,4,5])
