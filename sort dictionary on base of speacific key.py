def sort_dicts_by_key(dict_list, key):
    if not all(key in dictionary for dictionary in dict_list):
        raise ValueError(f"Not all dictionaries contain the key '{key}'")

    sorted_list = sorted(dict_list, key=lambda x: x[key])
    return sorted_list

dict_list = [
    {'name': 'Alice', 'score': 85},
    {'name': 'Bob', 'score': 92},
    {'name': 'Charlie', 'score': 87}
]

sorted_list = sort_dicts_by_key(dict_list, 'score')
print(sorted_list)