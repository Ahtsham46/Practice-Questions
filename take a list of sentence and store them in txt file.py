def sentence():
    sentence_list = []
    file = open("file.txt", 'a')
    while True:
        sentence = input("Enter a sentence: ")
        sentence_list.append(sentence + '\n')
        ch = input("Do you want to add more sentences? Y/N: ")
        if ch.lower() == 'n':
            break
    file.writelines(sentence_list)
    file.close()
    with open("file.txt", 'r') as f:
        print(f.read())

sentence()
