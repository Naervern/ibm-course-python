# This is a python file for the IBM DevOps course
# Maybe something will go here eventually, who knows?
# Anyways, this is one of the stupidest ways to print Hello, world! that I can think of right now

import time

for i in "Hello, world!":
    for c in range(30, 123):
        print(chr(c), end= "")
        time.sleep(0.05)
        if chr(c)==i:
            break
        else:
            print("\b", end="")
