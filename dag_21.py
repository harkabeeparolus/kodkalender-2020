#! /usr/bin/env python3

"""Unga programmerare kodkalender 2020, lucka 21"""
# https://ungaprogrammerare.se/kodkalender/lucka-21/

import itertools

from input_files.dag_21_input import lista


def pairwise(iterable):
    "Collect data into pairs"
    # s -> (s0,s1), (s1,s2), (s2, s3), ...
    # https://docs.python.org/3/library/itertools.html#itertools-recipes
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


def is_rainbow_number(number: int) -> bool:
    """Rainbow number is a palindrome, starts and ends with 1, and numbers
    increase in sequence by 0 or 1."""

    num_str = str(number)

    palindrome = num_str == num_str[::-1]
    has_ones = num_str[0] == num_str[-1] == "1"

    half_length = len(num_str) // 2
    half = num_str[:-half_length]
    pairs = [map(int, pair) for pair in pairwise(half)]
    in_sequence = all(0 <= (b - a) <= 1 for a, b in pairs)

    return palindrome and has_ones and in_sequence


non_rainbows = [n for n in lista if not is_rainbow_number(n)]

print(non_rainbows)
print(f"Icke regnbågsnummer: {len(non_rainbows)}")

# [11123532111, 1234555655554321, 11112232211111]
# Icke regnbågsnummer: 3
