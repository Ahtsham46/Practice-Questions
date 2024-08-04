def is_pangram(s):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    return alphabet.issubset(set(s.lower()))
string = "The quick brown fox jumps over the lazy dog"
print(is_pangram(string))  
