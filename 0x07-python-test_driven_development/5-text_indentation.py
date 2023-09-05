#!/usr/bin/python3
"""Defines a function text_indentation"""


def text_indentation(text):
    """
    function that prints a text with 2 new lines 
    after each of these characters: ., ? and :

        Args:
            @text (str): text is a string
    """
    index = 0
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while (i < len(text)):
        print(text[i], end='')
        if text[i] in ['.', '?', ':']:
            print('\n')
            j = i + 1
            while text[j] == ' ':
                i += 1
                j += 1
        i += 1
