from Database import Database
from argparse import *
import os
import sys
__version__ = "0.1.1"

if __name__ == "__main__":
    db = Database("vocab2.db")

    parser = ArgumentParser(prog="libpyflashcard",
                            description="libpyflashcard command line client, version " + __version__)
    parser.add_argument("-v", "--verbose", dest="verbose", help="Increase verbosity of output.", action='store_true')
    parser.add_argument("--init", help="Initialize a new database.")
    parser.add_argument("-l", "--list", help="Return a list of decks.", nargs='?')
    parser.add_argument("-a", "--add", help="Add a new deck.")
    parser.add_argument("-r", "--remove", help="Remove a deck by name.")
    parser.add_argument("-i", "--import", dest="import_", metavar="IMPORT", help="Import a new deck from csv file.")
    parser.add_argument("-e", "--export", help="Export a deck to csv file.")
    args = parser.parse_args()

    if args.verbose:
        print("verbose")
    if args.init:
        print("init")
    elif args.list:
        print("hi")
        cards = db.list_cards(args.list)
        print(cards)
    elif args.list == 0:
        decks = db.list_decks()
        print(decks)
    elif args.add:
        print("add")
    elif args.remove:
        print("remove")
    elif args.import_:
        print("import")
    elif args.export:
        print("export")



