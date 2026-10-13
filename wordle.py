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

    def __init__(self, letter, status=None):
        self.letter = letter
        self.status = status


class WordleGame:
    def __init__(self, target=None):
        """Note the inclusion of a settable 'target' for ease of testing."""
        self.word_list = WordList()
        if not target:
            target = self.word_list.random_word()
        self.target = target
        self.guesses = []

    def score_guess(self, guess):
        """Takes the guess argument, and stores a list of LetterResult objects (with appropriate statuses) in self.guesses"""
        score = []
        for index, letter in enumerate(guess):
            if self.target[index] == letter:
                score.append(LetterResult(letter, "Correct"))
            elif letter in self.target:
                score.append(LetterResult(letter, "Present"))
            else:
                score.append(LetterResult(letter, "Absent"))
        return score

    def is_over(self):
        """Check if six guesses have been made"""
        return len(self.guesses) >= 6

    def is_won(self):
        """Return True if the most recent guess was all Correct"""
        if len(self.guesses) == 0:
            return False
        else:
            for i in self.guesses[-1]:
                if i.status != "Correct":
                    return False
        return True

    def make_guess(self, guess):
        """Score the guess and add it to the list of guesses"""
        score = self.score_guess(guess)
        self.guesses.append(score)

    def check_valid(self, guess):
        """Return True is the guess is in the wordlist, and False if its not"""
        if self.word_list.contains(guess):
            return True
        return False

    def display_board(self):
        """Print the board, using uppers for correct letter, lowers for Present, and underscores for Absent"""
        for word in self.guesses:
            for letter in word:
                if letter.status == "Correct":
                    print(letter.letter, end="")
                elif letter.status == "Present":
                    print(letter.letter.lower(), end="")
                else:
                    print("_", end="")
            print()

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
