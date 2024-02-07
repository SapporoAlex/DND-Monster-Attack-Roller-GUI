# DND-Monster-Attack-Roller-GUI

<img src="MAR%20Assets/Other/preview.gif" width="200" height="400">

A Program made in Pygame. It's a convenient tool for dungeon masters. No need to check stats, roll dice or calculate. Just move the slim window to the side of your screen and press the buttons of the most commonly used monster attacks to see attack, damage, and other effects.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Author](#author)
- [License](#license)

## Features
- 16 of the most common monsters used in DND
- A button for each attack type with attack-appropriate sound effects upon pressing
- Slim design, allowing an uncluttered screen
- Text box details all relevant information of attack, such as poison effects
- Nat 20s give double base damage

## Requirements
- [pygame](https://pypi.org/project/pygame/)

## Usage
1. Install the required Python package:

   ```bash
   pip install pygame
   ```

2. Run the script:

   ```bash
   MonsterAttackRoller.py
   ```

## File Structure
- `MAR Assets`: Folder with mp3 files, png and jpg images
- `MonsterAttackRoller.py`: Python script for running the game
- `buttons.py`: Python module for the buttons used in the main file

## Author
Alex McKinley

## License
This project is licensed under the [MIT License](LICENSE).
