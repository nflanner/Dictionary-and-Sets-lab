#!/usr/bin/env python3

"""

Dict and Set lab from UWPCE module 5
executable using 'py dict_lab.py' in bash shell

"""

"""
Dictionaries 1
Create a dictionary containing “name”, “city”, and “cake” for “Chris” from “Seattle” who likes “Chocolate” (so the keys should be: “name”, etc, and values: “Chris”, etc.)

Display the dictionary.

Delete the entry for “cake”.

Display the dictionary.

Add an entry for “fruit” with “Mango” and display the dictionary.

Display the dictionary keys.

Display the dictionary values.

Display whether or not “cake” is a key in the dictionary (i.e. False) (now).

Display whether or not “Mango” is a value in the dictionary (i.e. True).
"""
d1 = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}
print(d1)
d1.pop("cake")
print(d1)
d1["fruit"] = "Mango"
print(d1.keys())
print(d1.values())
print("cake" in d1)
print("Mango" in d1.values())

