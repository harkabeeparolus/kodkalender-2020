#! /usr/bin/env python3

"""Unga programmerare kodkalender 2020, lucka 14"""
# https://ungaprogrammerare.se/kodkalender/lucka-14/

from itertools import combinations

from input_files.dag_14_input import artikelnummer

numbers = (str(num) for num in artikelnummer)
anagrams = [(i, j) for i, j in combinations(numbers, 2) if sorted(i) == sorted(j)]
assert len(anagrams) == 1

print(f"Artikelnummer: {anagrams.pop()}")
# Artikelnummer: ('95094', '59049')
