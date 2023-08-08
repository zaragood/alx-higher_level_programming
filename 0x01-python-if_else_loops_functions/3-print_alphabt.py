#!/usr/bin/python3
# program that prints the ASCII alphabet, in lowercase
# Print all the letters except q and e

alphabets = ""
for letter in range(97, 123):
    alpha = chr(letter)
    if alpha != 'q' and alpha != 'e':
        alphabets += alpha
print(alphabets)
