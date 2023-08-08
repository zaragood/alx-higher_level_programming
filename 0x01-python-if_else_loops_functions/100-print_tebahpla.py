#!/usr/bin/python3
# prints the ASCII alphabet, in reverse order

for i in range(25, -1, -1):
    if i % 2 == 0:
        print(chr(65 + i), end="")
    else:
        print(chr(65 + i).lower(), end="")
