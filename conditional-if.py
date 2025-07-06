#!/usr/bin/env python
"""author: @RZFeeser
   Learning about conditionals """

def main():
    """runtime code"""

    sky = "blue"   # sky = 'blue'

    # check if sky has a string value of blue
    if sky == "blue":
        print("Looks like the sky is blue")

    # if sky exists
    if sky:
        print("looks like the sky exists")

    sky = 99

    # if sky exists
    if sky:
        print("looks like the sky exists")

    sky = "orange"

    ## test if sky is blue or 99
    if sky == "blue":
        print("Looks like the sky is blue")
    if sky == 99:
        print("looks like the sky is 99")
    if sky != "blue" and sky != 99:
        print("looks like sky exsits but it is not blue or 99")    


    ## use if, elif and else
    if sky == "blue":
        print("Looks like the sky is blue")
    elif sky == 99:
        print("looks like the sky is 99")
    else:
        print("looks like sky exsits but it is not blue or 99")   


if __name__ == "__main__":
    main()