#!/usr/bin/env python
"""Author: @RZFeeser
   All about lists"""

def main():
    """runtime code"""

    #             0          1        2
    fruit = ["strawberry", "lime", "lemon"]  # 3 items
    print(fruit)   # ["strawberry", "lime", "lemon"]
    print(fruit[0])   # "strawberry"
    print(fruit[2])   # "lemon"
    print(fruit[-1])  # "lemon"
    print(fruit[-2])  # "lime"
    fruit.append("apple")  # ["strawberry", "lime", "lemon", "apple"]
    print(fruit) # ["strawberry", "lime", "lemon", "apple"]
    print(fruit[-1])  # "apple"
    
    #              0         1
    veggies = ["carrots", "beets"]   # 2 items
    print(veggies)

    fruit.extend(veggies)
    print(fruit)          # ["strawberry", "lime", "lemon", "apple", "carrots", "beets"]

if __name__ == "__main__":
    main()