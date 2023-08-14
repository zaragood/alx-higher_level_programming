#!/usr/bin/python3

def multiple_returns(sentence):
    tuple_list = []

    if sentence is None:
        return(len(sentence), None)
    else:
        length = len(sentence)
        tuple_list.append(length)
        tuple_list.append(sentence[0])

    result_tuple = tuple(tuple_list)
    return(result_tuple)
