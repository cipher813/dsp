def intersect_lists_2(list1, list2):
    a = set(list1+list2)
    b = set(list1)
    c = set(list2)
    return(c-(a-b))

intersect_lists_2([1,2,3],[3,4,5])
