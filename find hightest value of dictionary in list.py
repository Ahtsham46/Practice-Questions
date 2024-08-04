def find_highest_value(dict_list, key):
    if not dict_list:
        return None
    highest_dict = None
    highest_value = float('-inf')
    for dictionary in dict_list:
        if key in dictionary and dictionary[key] > highest_value:
            highest_value = dictionary[key]
            highest_dict = dictionary
    return highest_dict
dict_list = [
    {'name': 'Alice', 'score': 85},
    {'name': 'Bob', 'score': 92},
    {'name': 'Charlie', 'score': 87}
]
highest_dict = find_highest_value(dict_list, 'score')
print(highest_dict) 
