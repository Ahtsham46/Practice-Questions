def count_characters(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
input_string = "hello world"
result = count_characters(input_string)
print(result)
