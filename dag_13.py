#! /usr/bin/env python3

"""Unga programmerare kodkalender 2020, lucka 13"""
# https://ungaprogrammerare.se/kodkalender/lucka-13/

from input_files.dag_13_input import tallista


def number_ok(number: int) -> bool:
    "Validate a number"
    as_string = str(number)
    assert len(as_string) >= 2
    pairs = [
        (int(as_string[i]), int(as_string[i + 1])) for i in range(len(as_string) - 1)
    ]
    return all(a == b or a < b for a, b in pairs)


valid_numbers = [n for n in tallista if number_ok(n)]

print(f"Antal lussenissar: {len(valid_numbers)}")
# Antal lussenissar: 1937
