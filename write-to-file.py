#!/usr/bin/env python
"""Author: @RZFeeser
   Learning to use python to create a simple text file"""

def main():
    """runtime code"""
    with open("CodeWithFeeser.txt", "w") as myfile:   # open CodeWithFeeser.txt in WRITE mode
        myfile.write("First line of the file\n")      # appears in first line of CodeWithFeeser.txt
        print("Second line of the file", file=myfile) # appears on second line of CodeWithFeeser.txt
                                                      # note that no \n is necessary with print()

if __name__ == "__main__":
    main()