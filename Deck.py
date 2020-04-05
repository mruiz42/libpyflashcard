from Card import Card
from random import shuffle
class Deck:
    def __init__(self, cards: list, deck_id: str, vocab_language: str = "", definition_language: str = ""):
        self.cards: list = cards
        self.deck_id: str = deck_id
        self.vocab_language: str = vocab_language
        self.definition_language: str = definition_language
        self.size: int = len(self.cards)

    def add(self, card: Card):
        self.cards.append(card)
        self.size = len(self.cards)

    def remove(self, card: Card):
        self.cards.remove(card)
        self.size = len(self.cards)

    def shuffle(self):
        return shuffle(self.cards)
