# Write your code here
import random


class Hangman:
    _TITLE = "H A N G M A N"
    _FOOTER = (
        "Thanks for playing!\n"
        "We'll see how well you did in the next stage"
    )

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
    def footer(self):
        return self._FOOTER

    @property
    def completed(self):
        return self._tries == 0

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
        self._tries -= 1
        if ch not in (self._word or ""):
            return "No such letter in the word"
        self._inputs_data.add(ch)


hangman = Hangman()
print(hangman.title)
hangman.game()
while not hangman.completed:
    print()
    print(hangman.word)
    ch = input("Input a letter: ")
    msg = hangman.guess_char(ch)
    if msg is not None:
        print(msg)
print()
print(hangman.footer)
