#!/usr/bin/env python
"""Author: @RZFeeser
   Learning about import and random"""

## standard libraries
import random

## 3rd party imports



def main():
    """runtime code"""

    # set your own entropy
    # random.seed(123456789123456789)

    characters = ['Frodo', 'Samwise', 'Legolas', 'Boromir', 'Strider', 'Gandalf']

    character_info = {'Frodo': 'Hobbit', 'Samwise': 'Hobbit', 'Legolas': 'Wood Elf', 'Boromir': 'Human', 'Strider': 'Human', 'Gandalf': 'Maia'}

    # make a random selection from a list
    random_char = random.choice(characters)
    print(random_char)

    # make a random selection from a dict
    random_name, me_race = random.choice(list(character_info.items()))    # [('Frodo', 'Hobbit') ('samwise', 'hobbit')]
    print(f'Looks like {random_name} was selected and is a {me_race}')

if __name__ == "__main__":
    main()