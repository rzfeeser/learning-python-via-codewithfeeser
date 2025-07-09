#!/usr/bin/env python
"""Author: @RZFeeser
   learning about f-strings"""


def main():
    """runtime code"""

    # basic var insertion
    name = 'rzfeeser'
    print(f'Hello there {name}')   # fill in {name} with rzfeeser

    # arithmetic opertaions
    a = 5
    b = 2
    print(f'The sum of {a} and {b}: {a + b}')

    # floating point formatting
    pi = 3.14159
    print(f'Two decimal digits from pi: {pi:.2f}')   # Two decimal digits from pi: 3.14

    # string padding
    word = 'dragon'
    print(f'This will always be 10 characters: {word:*>10}')    # ****dragon

    # reach into a dict
    webster = {'name': 'Luna', 'class': 'Wizard'}
    print(f'The name of the character is {webster.get("name")}')   # luna
    print(f'The name of the character is {webster["name"]}')

    # using an expression in an f string
    health = 10
    print(f'Player Status: {"Alive" if health > 0 else "Dead"}')

    # fstrings for HTTP operations
    token = 'QWERTY'   # in production never put a secret in your code
    print(f'http://rzfeeser.com/service?token={token}')



if __name__ == "__main__":
    main()