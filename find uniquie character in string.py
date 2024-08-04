def unique_chars(strings):
    if not strings:
        return set()
    common_chars = set(strings[0])
    for string in strings[1:]:
        common_chars &= set(string)
    return common_chars
string_list = ["hello", "world", "hold"]
result = unique_chars(string_list)
print(result)  
