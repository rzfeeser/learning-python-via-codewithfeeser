#!/usr/bin/env python
"""Author: @RZFeeser
   Examples of fstrings"""


def main():
    """runtime code"""

    # basic var insertion
    name = "RZFeeser"
    print(f"hello {name}")

    # arithmatic operations
    a = 5
    b = 2
    print(f"The sum of {a} and {b}: {a + b}")

    # floating point formatting
    pi = 3.14159
    print(f"Pi rounded to two decimals {pi:.2f}")

    # padding
    word = "dragon"
    print(f"This will always be 10 characters: {word:*>10}")   # ****dragon

    # reaching to a dict
    webster = {'name': 'Luna', 'class': 'Wizard'}
    print(f"The name of the character is {webster.get('name')} whom is a powerful {webster['class']}")

    # using an expression in an f string
    health = 10
    print(f"Player status: {'Alive' if health > 0 else 'Dead'}")   # evaluate a conditional within an fstring


    # basic var insertion - http example
    token = "QWERTY1234"
    print(f"http://rzfeeser.com/service?token={token}&name=RZF")       # putting together an uri
    print("http://rzfeeser.com/service?token=" + token + "name=RZF")   # without fstrings

if __name__ == "__main__":
    main()