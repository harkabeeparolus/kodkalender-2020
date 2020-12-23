#! /usr/bin/env python3

"""Unga programmerare kodkalender 2020, lucka 15"""
# https://ungaprogrammerare.se/kodkalender/lucka-15/

import string


def shift_letter(letter: str, amount: int) -> str:
    "Shift a letter forward in the alphabet by a certain amount"
    sv_alfabet = string.ascii_lowercase + "åäö"
    new_position = (amount + sv_alfabet.index(letter)) % len(sv_alfabet)
    return sv_alfabet[new_position]


def password_change(password: str) -> str:
    "Generate a new password from the old one"
    return "".join(shift_letter(letter, pos + 1) for pos, letter in enumerate(password))


tomte_pw = "tomtemorärbäst"
for i in range(10):
    tomte_pw = password_change(tomte_pw)

print(f"Nytt lösenord: {tomte_pw}")
# Nytt lösenord: afnbzoåkbbycdo
