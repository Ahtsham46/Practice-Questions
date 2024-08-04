def pangram(s):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    string_set = set(s.lower())
    if alphabet.issubset(string_set):
        return "This is pangram"
    else:
        return "This is not pangram"
string = input("Enter a sentence: ")
print(pangram(string))