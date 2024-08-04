def average_value(dict_list, key):
    total = 0
    count = 0

    for dictionary in dict_list:
        if key in dictionary:
            total += dictionary[key]
            count += 1

    if count == 0:
        raise ValueError(f"No dictionaries contain the key '{key}'")

    return total / count

dict_list = [
    {'name': 'Alice', 'score': 85},
    {'name': 'Bob', 'score': 92},
    {'name': 'Charlie', 'score': 87}
]
avg_score = average_value(dict_list, 'score')
print(avg_score)  
