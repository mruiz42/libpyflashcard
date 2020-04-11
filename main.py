from Database import Database
from argparse import *
import os
import sys
__version__ = "0.1.2"

if __name__ == "__main__":
    db = Database("vocab2.db")

    parser = ArgumentParser(prog="libpyflashcard",
                            description="libpyflashcard command line client, version " + __version__,
                            epilog="More information at: <https://github.com/mruiz42/libpyflashcard>")

    parser.add_argument("-V", "--version", dest="VERSION", help="Display current running version of program.")
    parser.add_argument("-v", "--verbose", dest="VERBOSE", help="Increase verbosity of output.", action='store_true')

    subparsers = parser.add_subparsers(title="SUBPARSERS",
                                       description="Valid subcommands.",
                                       help="help")

    parser_list = subparsers.add_parser("list", help="Help")
    parser_list.add_argument("DECKID", nargs="*")

    parser_delete = subparsers.add_parser("delete")
    parser_delete.add_argument("DECKID", nargs="*")

    args = parser.parse_args()

    if args.VERBOSE:
        print("verbose")
    if len(args.DECKID) != 0:
        print('hi')
        for row in db.list_cards(' '.join(args.DECKID)):
            print(row)
    elif len(args.DECKID) == 0:
        print("hi")
        for row in db.list_decks():
            print(row)


