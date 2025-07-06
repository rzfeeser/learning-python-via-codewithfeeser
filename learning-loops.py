#!/usr/bin/env python3
"""Author: @RZFeeser
   Learning about for loops"""

def main():
    """runtime code"""

    american_astros = ["Buzz Aldrin", "Neil Armstrong", "Gordon Cooper"]  # 3 items (strings) in a list

    for astro in american_astros:
        print(astro)
        print("*******")

    groceries = {"milk": 1.00, "apple": 0.25, "orange": 0.45}

    for fooditem in groceries:    # looping across a dict by default looks ONLY at the keys (left)
        print(fooditem)

    for fooditem in groceries.keys():    # this is the same as the loop above
        print(fooditem)

    for prices in groceries.values():
        print(prices)

    
    for position in range(10):   # start at 0 work upto 9
        print(position)

if __name__ == "__main__":
    main()