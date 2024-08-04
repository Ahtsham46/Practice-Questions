def sort_strings(strings_list):
    return sorted(strings_list)
n = int(input("Enter the number of strings: "))
strings_list = []
for _ in range(n):
    string = input("Enter a string: ")
    strings_list.append(string)

sorted_list = sort_strings(strings_list)
    
print("Sorted list of strings:")
for string in sorted_list:
    print(string)
