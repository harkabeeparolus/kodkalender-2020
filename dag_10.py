#! /usr/bin/env python3

"""Unga programmerare kodkalender 2020, lucka 10"""
# https://ungaprogrammerare.se/kodkalender/lucka-10/

from input_files.dag_10_input import hacker_lista


def first_plus_last(num: int) -> int:
    "Sum first and last digits of an integer"
    s = str(num)
    return int(s[0]) + int(s[-1])


total = sum(first_plus_last(num) for num in hacker_lista)

print(f"Lösenord: {total}")
# Lösenord: 7233
