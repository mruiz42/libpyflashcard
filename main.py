from Database import Database
from argparse import *
import os
import sys

if __name__ == "__main__":
    parser = ArgumentParser(description="hi")
    parser.add_argument("--init")
    parser.add_argument("-l", "--list")
    parser.add_argument("-a", "--add")
    parser.add_argument("-r", "--remove")
    parser.add_argument("-i", "--import")
    parser.add_argument("-e", "--export")
    parser.add_argument("-h", "--help")
    db = Database("vocab2.db")

