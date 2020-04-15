from Statistic import Statistic


class Card:
    def __init__(self, card_id: int, deck_id: str, vocabulary: str, definition: str, pronunciation: str,
                 stat: Statistic, is_starred: bool):
        self.card_id: int = card_id
        self.deck_id: str = deck_id
        self.vocabulary: str = vocabulary
        self.definition: str = definition
        self.pronunciation: str = pronunciation
        self.stat: Statistic = stat
        self.is_starred: bool = is_starred

    def __str__(self):
        return (str(self.card_id) + ":" + self.vocabulary + ":" + self.definition + ":" + self.pronunciation
                + ":" + str(self.stat))

