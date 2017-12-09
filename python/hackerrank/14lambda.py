def list_evens(list):
    # listy = [n for n in list if n%2==0]
    listy = filter(lambda x: x%2==0, list)
    return listy

print(list_evens([3,4,7,2,9,170]))
