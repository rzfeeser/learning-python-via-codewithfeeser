#!/usr/bin/env python
"""Author: @RZFeeser
   Learning about Python dictionaries"""

def main():
    """runtime code"""

    tmnt = {}
    print(tmnt)  # {}

    tmnt = {"leader": "leonardo"} 
    print(tmnt)   # {"leader": "leonardo"}

    tmnt["inventor"] = "donatello"
    print(tmnt)    # {"leader": "leonardo", "inventor": "donatello"}

    # print(tmnt[0])  # this will cause an error
    print(tmnt["inventor"])   # "donatello"
    print(tmnt["leader"])     # "leonardo"

    tmnt["partydude"] = "shredder"
    print(tmnt)   # {"leader": "leonardo", "inventor": "donatello", "partydude" = "shredder"}
    tmnt["partydude"] = "michaelangelo"
    print(tmnt)   # {"leader": "leonardo", "inventor": "donatello", "partydude" = "michaelangelo"}

    # print(tmnt["attitude"])    # this will cause an error
    print(tmnt.get("attitude", None))        # .get() is a dict method
    print(tmnt.get("attitude", "That key is not found in the tmnt dictionary"))        # .get() is a dict method

    print(tmnt)
    del tmnt["partydude"]   # removes this key: value pair
    print(tmnt) # {"leader": "leonardo", "inventor": "donatello"}

    print(tmnt.keys())   # print all the keys
    print(tmnt.values()) # print all the values

if __name__ == "__main__":
    main()