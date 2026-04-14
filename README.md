# DnD Character Creator
A Python-based Dungeons & Dragons helper application with a graphical user interface.
This project was created for OOP coursework and implements character creation, ability score generation, health management, history loading, inventory, abilities, file saving/loading, and unit testing.

## Features
- Create a character with:
  - name
  - race
  - class
  - history
- Generate ability scores in three ways:
  - Standard Array
  - Dice Roll
  - Auto By Class
- Apply racial bonuses automatically
- Display a full character sheet with:
  - level
  - HP
  - AC
  - proficiency bonus
  - ability scores and modifiers
  - inventory
  - abilities
  - history
- Level up and reset level
- Heal and damage HP through the GUI
- Load history from a `.txt` file
- Save and load the latest hero using `game_data.xlsx`
- Store race and class data in Excel
- Unit tests for core functionality

## Technologies
- Python
- Tkinter
- Pandas
- OpenPyXL
- unittest

## Project structure
- `gui.py` - graphical user interface
- `models.py` - main classes and core object logic
- `score_methods.py` - ability score generation methods
- `storage.py` - reading and writing Excel data
- `test_kurs.py` - unit tests
- `game_data.xlsx` - race, class, and saved hero data
- `README.md` - project description

## OOP concepts used
This project applies all main OOP pillars:
- **Encapsulation**  
  Properties and setters are used in the `Character` class to validate values such as name, level, HP, history, inventory, and abilities.
- **Inheritance**  
  `StandardArrayMethod`, `DiceRollMethod`, and `AutoByClassMethod` inherit from the base `ScoreGenerationMethod` class.
- **Polymorphism**  
  Different score generation classes implement the same `generate()` method in different ways.
- **Abstraction**  
  The abstract behaviour of score generation is defined through the base `ScoreGenerationMethod` class.

## Design pattern
This project uses the **Factory Method** pattern.
The function `create_score_method()` returns the correct score generation object depending on the selected method:
- `StandardArrayMethod`
- `DiceRollMethod`
- `AutoByClassMethod`
This makes the program more flexible and easier to extend.
## Composition / Aggregation
The project demonstrates composition and aggregation:
- `Character` contains an `AbilityScores` object
- `Character` contains lists of `Item` and `Ability` objects
- `Character` stores connected race and class data
## How to run
1. Install dependencies:
```bash
pip install pandas openpyxl
```
2. Make sure all project files are in the same folder:
   - `gui.py`
   - `models.py`
   - `score_methods.py`
   - `storage.py`
   - `game_data.xlsx`
3. Run the program.
```bash
python gui.py
```
## How to use
1. Enter a character name.
2. Choose a class.
3. Choose a race.
4. Optionally load a history text file.
5. Select a score generation method.
6. Create the character.
7. View and manage the created hero in the character window.
8. Use buttons to:
   - level up
   - reset level
   - heal
   - deal damage
9. Save and reload the last hero from Excel.
## Testing
Core functionality is tested with `unittest`.
To run tests:
```bash
python -m unittest test_kurs.py
```
## Coursework goal
The goal of this project is to create a digital Dungeons & Dragons character helper while applying object-oriented programming principles, design patterns, file input/output, testing, and GUI development.

## Future improvements
- Editing inventory and abilities directly from the GUI
- Support for multiple saved heroes
- Better error handling for missing or invalid Excel data
- Expanded class and race database
- Improved user interface design
- Export to PDF or character sheet format

## Status
Coursework project completed and ready for further improvement