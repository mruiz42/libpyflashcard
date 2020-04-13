import argparse
import sys
import sqlite3
__version__ = "0.1.2"


class Interface(object):
    def __init__(self, db):
        self.db = db
        # Create main parser object
        cli = argparse.ArgumentParser(prog="libpyflashcard",
                            description="libpyflashcard command line client, version " + __version__,
        #                     usage="""main.py <command> [<args>]
        # Commands:
        # init       Initialize database
        # list       List cards/decks
        # create     Create a deck
        # remove     Remove a deck from database
        #                     """,
                            epilog="More information at: <https://github.com/mruiz42/libpyflashcard>")
        # Create parser options
        cli.add_argument("-V", "--version", dest="VERSION", help="display current running version of program.",
                         action='store_true')
        cli.add_argument("-v", "--verbose", dest="VERBOSE", help="increase verbosity of output.", action='store_true')
        cli.add_argument("command", help="subcommand to run.")
        args = cli.parse_args(sys.argv[1:2])
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
            card_list = self.db.list_cards(deckid)
            if len(card_list) == 0:
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
        if self.db.check_deck_exist(deckid):
            self.db.remove_deck(deckid)
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
            print("SUCCESS: \'" + deckid + "\' created.")
        else:
            print("ERROR: \'" + deckid + "\' already exists in database.")

    def init(self):
        pass
