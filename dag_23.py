#! /usr/bin/env python3

"""Unga programmerare kodkalender 2020, lucka 23"""
# https://ungaprogrammerare.se/kodkalender/lucka-23/

from itertools import zip_longest

from input_files.dag_23_input import kontrollbok


def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    # https://docs.python.org/3/library/itertools.html#itertools-recipes
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


GOOD_ENTRY = frozenset("IP")

for team, log_entry in enumerate(kontrollbok):
    if any(set(pair) != GOOD_ENTRY for pair in grouper(log_entry, 2)):
        print(f"Fel hos lag {team}: {log_entry}")

# Fel hos lag 73: IPPIIPIIPIPIIPPIIPIPPIIPIPIPIP
