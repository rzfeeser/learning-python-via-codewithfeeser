#!/usr/bin/env python3
"""Author: @RZFeeser
   Learning about Python Dictionaries"""

def main():
    """runtime code"""

    webster = {}  # creates an empty dict
    print(webster)  # {}

    webster = {"leader": "leonardo"}
    print(webster)   # {"leader": "leonardo"}
    print(webster["leader"])   # leonardo

             # key           # value
    webster["inventor"] = "donatello"

    print(webster)   #    {"leader": "leonardo", "inventor": "donatello"}

    webster["partydude"] = "michaelanglo"
    print(webster)   # {"leader": "leonardo", "inventor": "donatello", "partydude": "michaelanglo"}

    # print(webster["attitude"])  # this will cause an error!!

    print(webster.get("attitude"))   # if key is not found, then None is returned

    print(webster.get("teacher", "that key is not found in the dict"))  #   webster.get("teacher", None)

    print(webster)
    del webster["partydude"]  # this removes {"partydude": "michaelanglo"}
    print(webster)

if __name__ == "__main__":
    main()