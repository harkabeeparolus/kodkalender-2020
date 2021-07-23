#! /usr/bin/env python3

"""Unga programmerare kodkalender 2020, lucka 22."""
# https://ungaprogrammerare.se/kodkalender/lucka-22/

from input_files.dag_22_input import diktlista

known_letters = frozenset("abcdefghijklmno")

words = set(diktlista)
known_words = [word for word in words if set(word).issubset(known_letters)]

print(f"Eleverna kan {len(known_words)} ord av {len(words)}")
# Eleverna kan 39 ord av 271
