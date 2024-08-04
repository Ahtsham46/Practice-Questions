def intersection_lists(list1, list2):
    list1 = set(list1)
    list2 = set(list2)
    new_list = list(list1.intersection(list2))
    return new_list
list1 = [1, 3, 4, 5, 7]
list2 = [3, 4, 7, 2, 0]
print(intersection_lists(list1, list2))