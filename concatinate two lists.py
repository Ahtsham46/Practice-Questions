list1 = [1, 3, 4, 6, 7, 8]
list2 = [2, 5, 9, 10, 11]
# new_list = list1 + list2  this is other method
list1.extend(list2)
print(list1)