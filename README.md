# Matt Scroggs Math Puzzle Solutions

These are my solutions to many of the math puzzles created by [Matt Scroggs](https://www.mscroggs.co.uk/), written using LaTeX.
These include the yearly advent calendars, yearly Christmas cards, and the Sunday Afternoon Maths puzzles.
Also included are Python scripts for some puzzles to calculate or verify answers, as well as some useful Python utilities.

Each December I really enjoy working the advent and Christmas card puzzles, but I will not be posting the solutions for a given year until after the New Year when the competition is complete and Matt posts the answers.

## Puzzle Status

- **Advent 2015** - Complete.
- **Advent 2016** - Have old Python scripts for some of the puzzles but did not document the solutions. Currently working on getting these into the new format.
- **Christmas Card 2016** - Have an old Python script but no solutions. I plan to go back and complete this.
- **Advent 2017** - Have old Python scripts for some of the puzzles and solutions/answers crudely written in a text file. Currently the solutions document is just a placeholder, and I plan to go back and complete it.
- **Christmas Card 2017** - Completely undocumented. I plan to go back and complete this.
- **Advent 2018** - Have Python scripts and the solutions documented in a LibreOffice document. Plan to migrate this into the current LaTeX format.
- **Christmas Card 2018** - Have a Python script but no solutions document. I plan to go back and complete this.
- **Advent 2019** - Complete, but may revisit some puzzles to try to solve them analytically instead of by brute force with Python.
- **Christmas Card 2019** - Complete, but may revisit some puzzles to try to solve them analytically instead of by brute force with Python.
- **Advent 2020** - Complete.
- **Christmas Card 2020** - Complete.
- **Advent 2021** - Complete.
- **Christmas Card 2021** - Complete.
- **Advent 2022** - Complete.
- **Christmas Card 2022** - Complete.
- **Advent 2023** - Complete.
- **Christmas Card 2023** - Complete.
- **Sunday Afternoon Maths** - So far I have only solved very few of these, and just with a couple of stray Python scripts. Will go back and work on these once the advent and Christmas card puzzles are all in order.

## Logic Assistant

This is a GUI Python utility (uses PyQt5) that I developed to make it much easier to work through many of the puzzles that require careful logical deduction, including the various puzzles where the goal is to fill in grids of digits (e.g. the Dec 4 and Dec 6 puzzles from the 2015 advent calendar).
The script is `./logic_assistant.py`, and run this with `-h` to learn how to use it.

## Puzzle Directory

In solving puzzles, I have found it useful to be able to easily refer to puzzles I have already solved to see whether I can leverage previous solutions.
To facilitate this, I wrote a Python program that reads a database of puzzles and generates a LaTeX document with those puzzles (questions only).
Each puzzle has one or more tags and the Python program can filter on these tags to only show puzzles of interest.
This is all located in `./directory` and one can run `make help` from there to learn how to build a document that contains all or a subset of the puzzles based on tags.
