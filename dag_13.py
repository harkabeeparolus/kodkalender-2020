#! /usr/bin/env python3

"""Unga programmerare kodkalender 2020, lucka 13"""
# https://ungaprogrammerare.se/kodkalender/lucka-13/

import itertools

from input_files.dag_13_input import tallista


def pairwise(iterable):
    "Collect data into pairs"
    # s -> (s0,s1), (s1,s2), (s2, s3), ...
    # https://docs.python.org/3/library/itertools.html#itertools-recipes
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


def number_ok(number: int) -> bool:
    "Validate a number"
    num_str = str(number)
    assert len(num_str) >= 2
    pairs = [map(int, pair) for pair in pairwise(num_str)]
    return all(a == b or a < b for a, b in pairs)


valid_numbers = [n for n in tallista if number_ok(n)]

print(f"Antal lussenissar: {len(valid_numbers)}")
# Antal lussenissar: 1937
