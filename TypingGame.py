import os
import re
from Card import Card
from Deck import Deck
from Session import Session
from Statistic import Statistic
from Database import Database
class TypingGame:
    '''
    The TypingGame object controls the study game loop and user interactions via command line input.
    :param deck: The deck that will be studied by user during session.
    :type deck: Deck
    :param show_pronunciation: Boolean flag controlling whether or not to show the pronunciation string.
    :type show_pronunciation: bool
    :param is_shuffle: Boolean flag controlling whether or not to shuffle the card order.
    :type is_shuffle: bool
    '''
    def __init__(self, deck: Deck, db: Database, show_pronunciation: bool = False, is_shuffle: bool = False):
        self.db = db
        self.session = Session()
        self.show_pronunciation = show_pronunciation
        self.is_shuffle = is_shuffle
        self.deck = deck
        self.play()

    def play(self) -> None:
        """
        Main game loop for Typing Game
        :return: None
        """
        __TYPO__ = "!TYPO"
        __APPEND__ = "!APPEND"
        __HELP__ = "!HELP" # TODO
        __EDIT__ = "!EDIT" #TODO
        missed_cards = list()
        correct_cards = list()
        checkpoint_indices = list()
        index = 0
        # Create checkpoint indexes
        for i in range(0, len(self.deck.cards), 10):
            checkpoint_indices.append(i)
        # os.system('cls')  # on windows
        if self.is_shuffle:
            self.deck.shuffle()

        for card in self.deck.cards:
            os.system('clear')
            index += 1
            question = card.vocabulary
            if self.show_pronunciation:
                question += "(" + card.pronunciation + ")"
            question += "\nYour answer: "
            # Prompt user input
            user_input = input(question)
            valid_answers = self.sanitize_answers(card.definition)
            # Check answers
            if self.check_answer(user_input, valid_answers):
                print("Correct!")
                card.stat.num_correct += 1
                card.stat.num_attempts += 1
                input("Answer: " + card.definition + "\nPress ENTER to continue...")
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
                    if user_input == __APPEND__:
                        pass
                        # TODO: Add user_input to database definition
                    if self.check_answer(user_input, valid_answers):
                        if card not in missed_cards:
                            missed_cards.append(card)
                        card.stat.num_attempts += 1
                        break
            # check if at a checkpoint index
            if index in checkpoint_indices:
                self.checkpoint(missed_cards)

    def sanitize_answers(self, answer: str, delim: str=";") -> list:
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


        # TODO: Update database tables here #####################
        print("Missed words:\n")
        for card in missed_cards:
            print(card)
        print("Correct words:\n")

        input("Press ENTER to continue...")