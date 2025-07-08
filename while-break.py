#!/usr/bin/env python
"""Author: @RZFeeser
   while loops and break"""

# standard library
import random

def main():
    """runtime code"""

    me_char = ['Frodo', 'Samwise', 'Gandalf', 'Pippen', 'Strider']
    me_choice = ''

    print("Learning about while loops with conditionals")
    while me_choice != "Gandalf":
        print("As long as Gandalf is not chosen, we continue to loop!")
        me_choice = random.choice(me_char) # make a random selection
        print(me_choice) # display the the random selection

    print("Learning about while true")    
    while True:   # indefinite
        print("As long as Gandalf is not chosen, we continue to loop!")
        me_choice = random.choice(me_char)
        print(me_choice) # display the the random selection

        if me_choice == 'Gandalf':
            break # this will escape a while or for loop




if __name__ == "__main__":
    main()