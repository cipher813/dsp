def remove_adjacent(nums):
    listy = []
    for i in len(nums):
        if nums[i] != nums[i+1]:
            listy.append(nums[i])
        else:
            continue
    return listy

print(remove_adjacent([1,2,2,3]))
print(remove_adjacent([2,2,3,3,3,2]))
