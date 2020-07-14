# Write your code here
import random


class HangMan:
    _TITLE = "H A N G M A N"

    _DEFAULT_WORDS = ['python', 'java', 'kotlin', 'javascript']
    _DEFAULT_TIERS = 8

    def __init__(self, words=None, tires=None):
        self._words = self._DEFAULT_WORDS
        if words is not None:
            if isinstance(words, list):
                self._words.extend(words)
            else:
                self._words.append(words)

        self._tries = tires or self._DEFAULT_TIERS
        self._word = None
        self._inputs_data = set()

    @property
    def title(self):
        return self._TITLE

    @property
    def result(self):
        if self._tries == 0:
            return "You are hanged!"
        if self.completed:
            return (
                f"You guessed the word {self.word}!\n"
                f"You survived!"
            )

    @property
    def completed(self):
        return self.word == self._word or self._tries == 0

    @property
    def word(self):
        return "".join([(
            char if char in self._inputs_data else "-"
        ) for char in self._word or ""])

    def game(self, tires=None):
        self._word = random.choice(self._words)
        self._inputs_data.clear()
        self._tries = tires or self._DEFAULT_TIERS

    def guess_char(self, ch):
        if len(ch) > 1 or not ch:
            return "You should input a single letter"
        if not("a" <= ch <= "z"):
            return "It is not an ASCII lowercase letter"
        if ch in self._inputs_data:
            return "You already typed this letter"
        self._inputs_data.add(ch)
        if ch not in (self._word or ""):
            self._tries -= 1
            return "No such letter in the word"


hangman = HangMan()
print(hangman.title)
hangman.game()
while not hangman.completed:
    print()
    print(hangman.word)
    ch = input("Input a letter: ")
    msg = hangman.guess_char(ch)
    if msg is not None:
        print(msg)
print(hangman.result)
