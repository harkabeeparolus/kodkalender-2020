#! /usr/bin/env python3

"""Unga programmerare kodkalender 2020, lucka 6"""
# https://ungaprogrammerare.se/kodkalender/lucka-6/

import re

from dag_6_input import önskelista

SV_VOWELS = "aouåeiyäö"
FORBIDDEN_LETTERS = "cywh"
TWO_IN_A_ROW = re.compile(r"(.)\1")


def wish_ok(wish):
    conditions = (
        any(letter in SV_VOWELS for letter in wish),
        not any(letter in FORBIDDEN_LETTERS for letter in wish),
        TWO_IN_A_ROW.search(wish),
    )
    return all(conditions)


approved = [wish for wish in önskelista if wish_ok(wish)]

print(f"Antal julklappar: {len(approved)}")
# Antal julklappar: 71