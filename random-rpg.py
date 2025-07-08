#!/usr/bin/env python
"""Author: @RZFeeser
   Learning about Python via a simple RPG where a user is walking a road to Ravenmoore.
   The user presses ENTER to advance the game.
   Each turn one of three events may happen: enemy, item, or nothing
   If an enemy encounter begins, the user may type 'fight' or 'run'.
   Item signals that an item has been found.
   Nothing means nothing happens that turn."""

# standard library
import random


def main():
    """runtime code"""

    # game init
    inventory = [] # inventory
    health = 10    # health
    items = ['Sword', 'Shield', 'Healing Herbs']  # items that can be found
    enemies = ['Goblin', 'Skeleton', 'Wolf', 'Bandit']  # enemies

    # game starts -- runs by default for 20 turns (loop)
    for turn in range (1, 21):
        print(f'\nTurn {turn}: You take another step towards Ravenmoor')

        # when a turn begins, make a random decision as to what happens: enemy, item, or nothing (import random)
        event = random.choice(['nothing', 'item', 'enemy'])
        
        # check the results of the decision (if, elf)
        if event == 'nothing':
            print('The road is quiet. Nothing happens.')
        elif event == 'item':
            found_item = random.choice(items)  # select a random item from inventory
            if found_item == 'Healing Herbs':
                print(f"You found {found_item}! You use them to increase your HP by +1.")
                health += 1    # health = health + 1
            # if item -- add to inventory if it doesn't exist
            elif found_item not in inventory:
                inventory.append(found_item)  # add the item to your inventory
                print(f"You found {found_item}!")
            else:
                print(f"You found {found_item}! Unfortunately, you already one.")
        # if enemy -- ask user if they want to run or fight
        elif event == 'enemy':
            enemy = random.choice(enemies)   # pick randomly a bad guy
            print(f"An enemy appears: {enemy}") # tell user what they are up against
            action = input('Do you want to fight or run? (fight/run): ').lower()  # normalize input
            if action == 'fight':
                if 'Sword' in inventory:
                    print(f'You bravely fight the {enemy} and win thanks to your sword!')
                    if random.choice([True, False]):  # pick true or false
                        print(f'But you were injured in the fight and take -2 HP')
                        health -= 2   # health = health -2
                elif 'Shield' in inventory:
                    print(f'You faught bravely but with only a shield, the {enemy} injured you.')
                    health -= 2
                else:
                    print(f'You fight bravely but without a sword or shield you are injured.')
                    health -=3
            elif action == 'run':
                if random.choice([True, False]):
                    print('You managed to escape safely!')
                else:
                    print(f'The {enemy} catches up and hurts you as you run')
                    health -=2
            else:
                print(f'As you hesitate, the {enemy} attacks you for -3 HP')
                health -=3

        # display current user stats
        if health <= 0:
            print('\nYou have lost all of your health and collapse on the road to Ravenmoor.')
            break # when encountered within a loop, the loop ENDS

        print(f'Current health: {health}')
        print(f'Inventory: {inventory}')

        # ask user to press ENTER to move to next turn
        input(f'Press ENTER to move to the next turn')


    # game ends with a win at Ravenmoor
    if health > 0:
        print('\nCongratulations! You safely made it to Ravenmoor!')
    else:
        print('\nGame over. You did not reach the town of Ravenmoor.')



if __name__ == "__main__":
    main()