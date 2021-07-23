#! /usr/bin/env python3

"""Unga programmerare kodkalender 2020, lucka 6."""
# https://ungaprogrammerare.se/kodkalender/lucka-6/

import re

from input_files.dag_6_input import önskelista

SV_VOWELS = "aouåeiyäö"
FORBIDDEN_LETTERS = "cywh"
TWO_IN_A_ROW = re.compile(r"(.)\1")


def wish_ok(wish: str) -> bool:
    """See if all conditions are approved for a single wish."""
    one_vowel = any(letter in SV_VOWELS for letter in wish)
    two_letters = TWO_IN_A_ROW.search(wish) or False
    no_forbidden = not any(letter in FORBIDDEN_LETTERS for letter in wish)

    return one_vowel and two_letters and no_forbidden


approved = [wish for wish in önskelista if wish_ok(wish)]

print(f"Antal julklappar: {len(approved)}")
# Antal julklappar: 71
