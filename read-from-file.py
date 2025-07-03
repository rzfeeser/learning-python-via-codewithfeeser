#!/usr/bin/env python
"""Author: @RZFeeser
   Writing a python script that reads from a file"""

def main():
    """runtime code"""
    with open("OpenMe.txt", "r") as myfile:
        print(myfile.read())  # display to the screen all the contents of myfile

if __name__ == "__main__":
    main()