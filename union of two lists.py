list1 = [1, 3, 5, 6]
list2 = [1, 3, 4, 2]
new_list = list(set(list1).union(set(list2)))
print(f'union of two list: {new_list}')