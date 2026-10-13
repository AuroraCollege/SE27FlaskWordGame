# Build your OOP Wordle clone here

import random


class WordList:
    def __init__(self):
        words = open("wordlist.txt")
        wordList = []
        for word in words:
            if len(word) == 6:
                word.strip().upper()
                if not word.__contains__("-"):
                    wordList.append(word.strip().upper())
        self.words = wordList

    def contains(self, word):
        target = word.strip().upper()
        return target in self.words

    def random_word(self):
        return random.choice(self.words)
