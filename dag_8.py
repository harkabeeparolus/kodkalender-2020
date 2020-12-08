#! /usr/bin/env python3

"""Unga programmerare kodkalender 2020, lucka 8"""
# https://ungaprogrammerare.se/kodkalender/lucka-8/

import string
from typing import Iterable

from dag_8_input import krypterad_önskelista


def rotate_right(seq: str, amount: int) -> str:
    """Right rotate a string, and return the result."""

    return seq[-amount:] + seq[:-amount]


def decrypt(seq: Iterable[str]) -> Iterable[str]:
    """Decrypt a list of strings, and yield the result as an iterator."""

    sv_alfabet = string.ascii_lowercase + "åäö"
    key = dict(zip(sv_alfabet, rotate_right(sv_alfabet, 13)))
    
    for crypt_phrase in seq:
        yield "".join(key[letter.lower()] for letter in crypt_phrase)


for wish in decrypt(krypterad_önskelista):
    print(wish)

# flygplan
# basketbollspump
# undervattenskamera
