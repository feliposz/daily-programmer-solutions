"""
[2/12/2012] Challenge #4 [easy]
http://www.reddit.com/r/dailyprogrammer/comments/pm6oj/2122012_challenge_4_easy/

You're challenge for today is to create a random password generator!
For extra credit, allow the user to specify the amount of passwords to generate.
For even more extra credit, allow the user to specify the length of the strings he wants to generate!
"""

from sys import argv
from string import ascii_letters, digits
from random import sample

count = 1 if len(argv) < 2 else int(argv[1])
size = 16 if len(argv) < 3 else int(argv[2])

for n in range(count):
    print(''.join(sample(ascii_letters+digits, size)))
