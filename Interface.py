import argparse
import sys
from TypingGame import TypingGame
from CsvTool import CsvTool
import datetime
import sqlite3

class Interface(object):
    def __init__(self, db, version):
        self.db = db
        # Create main parser object
        cli = argparse.ArgumentParser(prog="libpyflashcard",
                            description="libpyflashcard command line client, version " + version,
                            usage="""main.py <command> [<args>]\nCommands:
        \ninit       Initialize database.
        \nlist       List cards/decks.
        \ncreate     Create a deck.
        \ndelete     Remove a deck from database.
        \nimport     Import a deck from csv.
        \nexport     Export a deck to csv.
        \nstudy      Study a deck.
                            """,
                            epilog="More information at: <https://github.com/mruiz42/libpyflashcard>")
        # Create parser options
        cli.add_argument("-V", "--version", dest="VERSION", help="display current running version of program.",
                         action='store_true')
        cli.add_argument("-v", "--verbose", dest="VERBOSE", help="increase verbosity of output.", action='store_true')
        cli.add_argument("command", help="command to be run. See available commands above.")
        args = cli.parse_args(sys.argv[1:2])
        if args.command == "import":
            args.command = "import_"
        if not hasattr(self, args.command):
            print("Unrecognized command")
            cli.print_help()
            exit(1)
        getattr(self, args.command)()

    def list(self):
        cli = argparse.ArgumentParser(description="return a list of decks or cards.")
        cli.add_argument("deckid", nargs="*")
        args = cli.parse_args(sys.argv[2:])
        deckid = ' '.join(args.deckid)
        if len(args.deckid) != 0:
            card_list = self.db.get_deck(deckid)
            if len(card_list.cards) == 0:
                print("Nothing to show.")
            else:
                for row in card_list:
                    print(row)
        elif len(args.deckid) == 0:
            if len(self.db.list_decks()) == 0:
                print("Nothing to show.")
            else:
                deck_list = self.db.list_decks()
                for row in deck_list:
                    print(row)

    def delete(self):
        cli = argparse.ArgumentParser(description="delete a deck from database.")
        cli.add_argument("deckid", nargs="*")
        args = cli.parse_args(sys.argv[2:])
        deckid = ' '.join(args.deckid)
        if len(deckid) == 0:
            deckid = input("Enter name of deck you would like to delete: ")
        #if self.db.check_deck_exist(deckid):
        #TODO: need to fix check_deck_exist() its broken! !
        if True:
            self.db.remove_deck(deckid)
            self.db.commit()
            print("SUCCESS: \'" + deckid + "\' removed from database.")
        else:
            print("ERROR: \'" + deckid + "\' does not exist in database.")

    def create(self):
        cli = argparse.ArgumentParser(description="create a new deck.")
        cli.add_argument("deckid", nargs="*")
        args = cli.parse_args(sys.argv[2:])
        deckid = ' '.join(args.deckid)
        if len(deckid) == 0:
            deckid = input("Enter name of deck you would like to create: ")
        if not self.db.check_deck_exist(deckid):
            self.db.create_deck(deckid)
            self.db.commit()
            print("SUCCESS: \'" + deckid + "\' created.")
        else:
            print("ERROR: \'" + deckid + "\' already exists in database.")

    def init(self):
        self.db.initialize()
        self.db.commit()

    def import_(self):
        # TODO: Finish
        deckid = ""
        vocab_language = ""
        definition_language = ""
        cli = argparse.ArgumentParser(description="create a new deck.")
        cli.add_argument("FILENAME", nargs="*")
        cli.add_argument("--name", "-n", nargs="*", dest="NAME", help="specify the name of a deck you want to import.")
        args = cli.parse_args(sys.argv[2:])
        filename = ' '.join(args.FILENAME)
        deckid = ' '.join(args.NAME)
        if len(filename) == 0:
            filename = input("Enter filename or path you would like to import: ")
        csv = CsvTool(filename)
        rows = csv.get_data()
        for row in rows:
            row.insert(0, deckid)
            row.insert(1, 0)
        languages = self.language_prompt()
        n_languages = len(languages) - 1
        dc = 0
        vc = 0
        while vc <= 0 or vc > n_languages:
            vc = int(input("Vocabulary language (1-" + str(n_languages) + "): "))
        vocab_language = languages[vc]
        while dc <= 0 or dc > n_languages:
            dc = int(input("Definition language (1-" + str(n_languages) + "): "))
        definition_language = languages[dc]

        # if self.db.check_deck_exist(deckid):
        #TODO: check_deck_exists() is broken!! this is a bandaid fix
        if True:
            self.db.create_deck(deckid, vocab_language, definition_language)
            self.db.add_many_cards_to_deck(rows)
            self.db.commit()
            print("SUCCESS: \'" + deckid + "\' created.")
        else:
            print("ERROR: \'" + deckid + "\' already exists in database.")




    def study(self):
        cli = argparse.ArgumentParser(description="start a new study session.")
        cli.add_argument("deckid", nargs="*")
        cli.add_argument("--pronunciation", dest="PRONUNCIATION", action="store_true")
        cli.add_argument("--shuffle", dest="SHUFFLE", action="store_true")
        args = cli.parse_args(sys.argv[2:])
        deckid = ' '.join(args.deckid)
        if len(deckid) == 0:
            deckid = input("Enter name of deck you would like to study: ")
        deck = self.db.get_deck(deckid)
        if len(deck.cards) > 0:
            TypingGame(deck, self.db, args.PRONUNCIATION, args.SHUFFLE)
        else:
            print("ERROR: \'" + deckid + "\' does not exists in database.")




    def language_prompt(self) -> list:
        languages = ["", "Chinese (Simplified)", "Chinese (Traditional)", "Chinese (Pinyin)", "Spanish", "English", "Hindi", "Arabic",
                          "Portuguese", "Russian", "Japanese", "Japanese (Romanji)", "Punjabi", "German", "Javanese", "Malay", "Telugu",
                          "Vietnamese", "Korean", "French", "Turkish", "Italian", "Thai", "Persian", "Polish",
                          "Romanian", "Dutch", "Czech", "Swedish"]
        for i in range(1, len(languages)):
            print(str(i) + "\t" + languages[i])

        return languages
