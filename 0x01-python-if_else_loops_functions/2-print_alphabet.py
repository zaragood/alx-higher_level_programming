#!/usr/bin/python3
# iprogram that prints the ASCII alphabet, in lowercase
alphabets = ""
for letter in range(97, 123):
    alphabets += chr(letter)
print("{}".format(alphabets))
