#!/usr/bin/env python
"""Author: @RZFeeser
   Learning about collecting input()"""

def main():
    """runtime code"""

    # set the store inventory
    inventory = {"apple": 0.5, "banana": 0.5, "milk": 1.00, "bread": 3.00}

    # welcome our users
    print("Welcome to our store!")
    print("Currently available is...")

    # display what is in the store
    for fooditem in inventory:
        print(fooditem)

    # grab string input from user
    item_to_check = input("What price would you like to check? ").lower()

    # determine how to respond to customer
    if item_to_check in inventory:
        print("The price of", item_to_check, "is", inventory.get(item_to_check))
    else:
        print("The store does not carry", item_to_check)


if __name__ == "__main__":
    main()