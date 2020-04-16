# libpyflashcard [![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/) [![HitCount](http://hits.dwyl.com/mruiz42/libflashcard.svg)](http://hits.dwyl.com/mruiz42/libpyflashcard)

A simple library written in python for storing flashcard data in a sqlite database. 
## Features
To be documented later

## Getting started
#### Requirements
* sqlite3
* python3
#### Compilation & running
For now, get started with `python3 main.py --help`
## Documentation
https://libflashcard.readthedocs.io/en/latest/
## Useful commands
##### Initialize database
`python3 main.py init`
##### Listing content
`python3 main.py list` - returns a list of decks inside database.
<br>`python3 main.py list <DECK NAME>` - returns a list of cards within specified deck. </br>
##### Importing from csv
`python3 main.py import <CSV PATH>`
##### Create a new empty deck
`python3 main.py create <DECK NAME>` 
##### Delete a deck of cards and associated data
`python3 main.py delete <DECK NAME>`
##### Study
`python3 main.py study <DECK NAME>`




## Database structure
##### DECKS
* CARD_ID (Primary key)
* DECK_ID
* IS_STARRED
* VOCABULARY
* DEFINITION
* PRONUNCIATION
* IMAGE_DATA
##### LANGUAGES
* LANGUAGE_NAME
##### CARDS
* DECK_ID
* VOCABULARY_LANGUAGE
* DEFINITION_LANGUAGE
##### SESSIONS
* START_TIME
* DECK_ID
##### STATISTICS
* CARD_ID
* DECK_ID
* START_TIME
* TIMES_CORRECT
* TIMES_ATTEMPTED
<br></br>
<br></br>
<br></br>
<br></br>

## MIT License

Copyright (c) 2020 Michael Ruiz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
