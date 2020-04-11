import sqlite3
from Card import Card
import os


class Database:
    def __init__(self, path: str):
        self.path = path
        self.db = sqlite3.connect(self.path)
        self.cur = self.db.cursor()
        self.db.text_factory = str

    def close(self):
        self.db.close()

    def initialize(self):
        statement = ("CREATE TABLE IF NOT EXISTS CARDS "
                     "(CARD_ID INTEGER PRIMARY KEY AUTOINCREMENT,"
                     "DECK_ID TEXT NOT NULL,"
                     "IS_STARRED BOOLEAN,"
                     "VOCABULARY TEXT,"
                     "DEFINITION TEXT,"
                     "PRONUNCIATION TEXT,"
                     "IMAGE_DATA BLOB,"
                     "FOREIGN KEY(DECK_ID) REFERENCES DECKS(DECK_ID));")
        self.db.execute(statement)
        self.db.commit()
        statement = ("CREATE TABLE IF NOT EXISTS DECKS "
                     "(DECK_ID TEXT PRIMARY KEY,"
                     "VOCABULARY_LANGUAGE TEXT,"
                     "DEFINITION_LANGUAGE TEXT);")
        self.db.execute(statement)
        self.db.commit()
        statement = ("CREATE TABLE IF NOT EXISTS SESSIONS"
                     "(START_TIME DATE PRIMARY KEY,"
                     "DECK_ID TEXT, "
                     "SESSION_TYPE TEXT, "
                     "FOREIGN KEY(DECK_ID) REFERENCES DECKS(DECK_ID));")
        self.db.execute(statement)
        self.db.commit()
        statement = ("CREATE TABLE IF NOT EXISTS STATISTICS"
                     "(CARD_ID INTEGER,"
                     "DECK_ID TEXT,"
                     "START_TIME DATE,"
                     "TIMES_CORRECT INTEGER,"
                     "TIMES_ATTEMPTED INTEGER,"
                     "FOREIGN KEY(CARD_ID) REFERENCES CARDS(CARD_ID),"
                     "FOREIGN KEY(DECK_ID) REFERENCES DECKS(DECK_ID),"
                     "FOREIGN KEY(START_TIME) REFERENCES SESSIONS(START_TIME));")
        self.db.execute(statement)
        self.db.commit()
        statement = ("CREATE TABLE IF NOT EXISTS LANGUAGES (LANGUAGE_NAME TEXT);")
        self.db.execute(statement)
        self.db.commit()

    def list_decks(self):
        statement = ("SELECT * FROM DECKS;")
        self.cur.execute(statement)
        decks = self.cur.fetchall()
        return decks

    # TODO: Check this
    def list_cards(self, deck_id: str) -> list:
        statement = ("SELECT * FROM CARDS WHERE DECK_ID=(?)")
        bind = (deck_id, )
        cur = self.db.execute(statement, bind)
        cards = cur.fetchall()
        return cards

    def create_deck(self, deck_id: str, vocab_language: str, definition_language: str):
        statement = ("INSERT INTO DECKS VALUES(?, ?, ?);")
        bind = (deck_id, vocab_language, definition_language, )
        self.db.execute(statement, bind)
        self.db.commit()

    def list_languages(self):
        statement = ("SELECT * FROM LANGUAGES;")
        self.db.execute(statement)
        languages = self.db.cursor().fetchall()
        return languages

    def remove_deck(self, deck_id: str):
        bind = (deck_id, )
        statement = "DELETE FROM STATISTICS WHERE (DECK_ID=?)"
        self.db.execute(statement, bind)
        statement = "DELETE FROM SESSIONS WHERE (DECK_ID=?)"
        self.db.execute(statement, bind)
        statement = "DELETE FROM CARDS WHERE (DECK_ID=?)"
        self.db.execute(statement, bind)
        statement = "DELETE FROM DECKS WHERE (DECK_ID=?)"
        self.db.execute(statement, bind)
        self.db.commit()

    def check_deck_exist(self, deck_id: str) -> bool:
        bind = (deck_id, )
        statement = ("SELECT * FROM DECKS WHERE DECK_ID=(?)")
        self.db.execute(statement, bind)
        decks = self.db.cursor().fetchall()
        return len(decks) > 0

    def export_file(self, path: str, delim: str = ""):
        pass

    def import_file(self):
        pass

    def add_card_to_deck(self, card: Card):
        bind = (card.deck_id, card.is_starred, card.vocabulary, card.definition, card.pronunciation, )
        statement = ("INSERT INTO CARDS (DECK_ID, IS_STARRED, VOCABULARY, DEFINITION, PRONUNCIATION)"
                     "VALUES(?, ?, ?, ?, ?);")
        self.db.execute(statement, bind)
        self.db.commit()

    def add_card_to_deck_v2(self, deck_id: str, is_starred: bool, vocabulary: str, definition: str, pronunciation: str):
        bind = (deck_id, is_starred, vocabulary, definition, pronunciation, )
        statement = ("INSERT INTO CARDS (DECK_ID, IS_STARRED, VOCABULARY, DEFINITION, PRONUNCIATION)"
                     "VALUES(?, ?, ?, ?, ?);")
        self.db.execute(statement, bind)
        self.db.commit()

    def add_many_cards_to_deck(self, cards: tuple):
        statement = ("INSERT INTO CARDS (DECK_ID, IS_STARRED, VOCABULARY, DEFINITION, PRONUNCIATION)"
                     "VALUES(?, ?, ?, ?, ?);")
        self.db.executemany(statement, cards)