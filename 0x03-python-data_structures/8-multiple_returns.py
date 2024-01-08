#!/usr/bin/python3

def multiple_returns(sentence):
    """Function that returns a tuple, the lenght and the first char of str"""

    len_sentence = len(sentence)
    first_char_sentence = sentence[0]

    return (len_sentence, first_char_sentence)
