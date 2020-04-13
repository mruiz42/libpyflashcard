from Database import Database
from Interface import Interface
from argparse import *
import os
import sys

__version__ = "0.1.2"
__database__ = "vocab2.db"


def delete():
    print('hi')


if __name__ == "__main__":
    # Load database from file
    db = Database(__database__)
    cli = Interface(db)
    # Create subparsers object
    # sub_cli = cli.add_subparsers(title="Commands")
    # # list command
    # sub_cli_list = sub_cli.add_parser("list", help="return a list of decks or cards.")
    # # parser_list.add_argument("deckid", nargs="*")
    # # parser_list.set_defaults(func=list)
    # # delete command
    # sub_cli_delete = sub_cli.add_parser("delete", help="delete a deck of cards.")
    # sub_cli_delete.add_argument('deckid', nargs="*")
    # # parser_delete.set_defaults(func=delete)

    # Parse users arguments
    # args = cli.parse_args()
