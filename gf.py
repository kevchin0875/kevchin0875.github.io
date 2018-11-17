WORDLIST_FILENAME = "word.txt"

def load_words():
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    return wordlist

word_list = load_words()
