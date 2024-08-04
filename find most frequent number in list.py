def most_frequent(lst):
    if not lst:
        return None

    frequency_dict = {}
    max_count = -1
    most_frequent_element = None

    for element in lst:
        if element in frequency_dict:
            frequency_dict[element] += 1
        else:
            frequency_dict[element] = 1

        if frequency_dict[element] > max_count:
            max_count = frequency_dict[element]
            most_frequent_element = element

    return most_frequent_element
my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(most_frequent(my_list))
