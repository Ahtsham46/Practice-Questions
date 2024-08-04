sentence = input("Enter a sentence: ")
word = input("Enter a word: ")
sentence = sentence.split()
if word in sentence:
    print(f"{word} word present in sentence.")
else:
    print(f"{word} word not present in sentence.")
