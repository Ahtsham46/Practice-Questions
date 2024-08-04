def remove_duplicate(s):
    
    result = []
    seen = set()
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)

# Input string
string = input("Enter a string: ")

# Remove duplicates and print the result
unique_string = remove_duplicate(string)
print(f"The string after removing duplicates is: {unique_string}")
