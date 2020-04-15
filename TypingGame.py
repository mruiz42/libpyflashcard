import os
import re
from Card import Card
from Deck import Deck
from Session import Session
from Statistic import Statistic

class TypingGame:
    def __init__(self, deck: Deck):
        self.session = Session()
        self.deck = deck
        self.play()

    def play(self) -> None:
        __TYPO__ = "!TYPO"
        missed_cards = list()
        checkpoint_indices = list()
        index = 0
        for i in range(0, len(self.deck.cards), 10):
            checkpoint_indices.append(i)
        # os.system('cls')  # on windows
        for card in self.deck.cards:
            os.system('clear')
            index += 1
            user_input = input(card.vocabulary + ":")
            valid_answers = self.sanitize_answers(card.definition)
            if self.check_answer(user_input, valid_answers):
                print("Correct!")
                card.stat.num_correct+=1
                card.stat.num_attempts+=1
                input("Answer: " + card.definition + "\nPress any key to continue...")
            else:
                os.system('clear')
                print("Incorrect")
                user_input = ""
                while True:
                    user_input = input("Answer: " + card.definition + "\nEnter the correct answer or '!TYPO': ")
                    if user_input == __TYPO__:
                        if card in missed_cards:
                            missed_cards.remove(card)
                        break
                    if self.check_answer(user_input, valid_answers):
                        if card not in missed_cards:
                            missed_cards.append(card)
                        card.stat.num_attempts += 1
                        break
            # check if at a checkpoint index
            if index in checkpoint_indices:
                self.checkpoint(missed_cards)

    def sanitize_answers(self, answer: str, delim: str="; ") -> list:
        """This function will take a delimited answer string and create a list
            while also sanitizing any punctuation characters and uppercase"""
        split_list = answer.split(delim)
        sanitize_list = list()
        for word in split_list:
            word = re.sub('\W+', '', word)
            word = word.lower()
            sanitize_list.append(word)
        return sanitize_list

    def check_answer(self, user_input: str, valid_answers: list) -> bool:
        user_list = self.sanitize_answers(user_input)
        for ul in user_list:
            for va in valid_answers:
                if ul == va:
                    return True
        return False

    def checkpoint(self, missed_cards: list):
        os.system('clear')
        print("Missed words:\n")
        for card in missed_cards:
            print(card)

        input("Press ENTER to continue...")