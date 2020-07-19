from Database import Database
from Interface import Interface
from argparse import *
import os
import sys

__version__ = "0.1.2"
__database__ = "vocab2.db"

if __name__ == "__main__":
    # Load database connection from file
    db = Database(__database__, __version__)
    # Initialize interface connection
    Interface(db)
