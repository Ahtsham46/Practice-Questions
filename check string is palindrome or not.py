def palindrome(s):
    cleaned_s = ''.join(char.lower() for char in s if char.isalnum())
    reversed_s = cleaned_s[::-1]
    return cleaned_s == reversed_s
string1 = "A ball, A pen"
print(palindrome(string1))