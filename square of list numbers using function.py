def squr_number(num):
    new_list = []
    for i in num:
        new_list.append(i**2)
    return new_list
list = [2, 1, 5, 6, 7, 8]
print(squr_number(list))