import os
from Card import Card
from Deck import Deck
from Session import Session
from Statistic import Statistic

class TypingGame:
    def __init__(self, deck: Deck):
        self.session = Session()
        self.stat = Statistic()
        self.deck = deck
        self.play()

    def play(self):
        # os.system('cls')  # on windows
        for card in self.deck.cards:
            os.system('clear')
            user_input = input(card.vocabulary + ":")
            valid_answers = card.definition.split("; ")
            if user_input in valid_answers:
                print("Correct!")
                self.stat.num_correct+=1
                self.stat.num_attempts+=1
            else:
                print("Incorrect")
                self.stat.num_attempts+=1
            input("Answer: " + card.definition + "\nPress any key to continue...")
