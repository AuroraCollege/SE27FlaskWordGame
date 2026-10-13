import random


class WordList:
    def __init__(self):
        wordlist = open("wordlist.txt")
        self.words = []
        for word in wordlist:
            if len(word) == 6:
                word.strip().upper()
                if not word.__contains__("-"):
                    self.words.append(word.strip().upper())

        longlist = open("long_wordlist.txt")
        self.longlist = []
        for word in longlist:
            self.longlist.append(word.strip().upper())

    def contains(self, word):
        target = word.strip().upper()
        return target in self.longlist

    def random_word(self):
        return random.choice(self.words)


class LetterResult:
    """Stores the letter and status for each letter result"""

    pass


class WordleGame:
    def __init__(self, target=None):
        """Note the inclusion of a settable 'target' for ease of testing."""
        pass

    def score_guess(self, guess):
        """Takes the guess argument, and stores a list of LetterResult objects (with appropriate statuses) in self.guesses"""
        pass

    def is_over(self):
        """Check if six guesses have been made"""
        pass

    def is_won(self):
        """Return True if the most recent guess was all Correct"""
        pass

    def make_guess(self, guess):
        """Score the guess and add it to the list of guesses"""
        pass

    def check_valid(self, guess):
        """Return True is the guess is in the wordlist, and False if its not"""
        pass

    def display_board(self):
        """Print the board, using uppers for correct letter, lowers for Present, and underscores for Absent"""
        pass

    def play(self):
        """The play method allows playing a text based version of the game. It relies on the other methods being implemented correctly..."""
        print(self.target)
        while not self.is_won() and not self.is_over():
            guess = input("Guess a word:").upper()
            if self.check_valid(guess):
                self.make_guess(guess)
            else:
                print(f"{guess} is not a valid word.")
            self.display_board()
        if self.is_won():
            print("Well done, you won!")
        else:
            print("Better luck next time!")


if __name__ == "__main__":
    w = WordleGame()
    w.play()
