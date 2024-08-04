def remove_vowel(s):
    vowels = "aeiouAEIOU"
    result = []
    for n in s:
        if n not in vowels:
            result.append(n)
    return ''.join(result)

string = input("Enter a string: ")
print(remove_vowel(string))
