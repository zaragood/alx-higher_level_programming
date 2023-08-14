#!/usr/bin/python3

def multiple_returns(sentence):
    tuple_list = []

    if sentence is None:
        length = len(sentence)
        tuple_list.append(length)
        tuple_list.append(None)
        result_tuple = tuple(tuple_list)
        return(result_tuple)
    else:
        length = len(sentence)
        tuple_list.append(length)
        tuple_list.append(sentence[0])

    result_tuple = tuple(tuple_list)
    return(result_tuple)
