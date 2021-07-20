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

"""
Dictionaries 2

Using the dictionary from item 1: Make a dictionary using the same keys but with the number 
of ‘t’s in each value as the value (consider upper and lower case?).

"""

d2 = dict([(k, v.lower().count('t')) for k, v in d1.items()])

"""
Sets 

Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible by 2, 3 and 4 (figure out a way to compute those – don’t just type them in).

Display the sets.

Display if s3 is a subset of s2 (False)

and if s4 is a subset of s2 (True).
"""

s2 = {i for i in range(21) if i % 2 == 0}
s3 = {i for i in range(21) if i % 3 == 0}
s4 = {i for i in range(21) if i % 4 == 0}

print("s1: {}\ns2: {}\ns3: {}".format(s2, s3, s4))
print(s2 < s3)
print(s4 < s2)

"""
Sets 2

Create a set with the letters in ‘Python’ and add ‘i’ to the set.

Create a frozenset with the letters in ‘marathon’.

Display the union and intersection of the two sets.
"""

s5 = {i for i in 'Python'}
s5.add('i')

s6 = frozenset('marathon')
print(s5 | s6)
print('Union of s5 and s6: {}'.format(s5 | s6))
print('Intersection of s5 and s6: {}'.format(s5 & s6))