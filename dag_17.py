#! /usr/bin/env python3

"""Unga programmerare kodkalender 2020, lucka 17."""
# https://ungaprogrammerare.se/kodkalender/lucka-17/

from input_files.dag_17_input import tallista

TOI_KEY = str.maketrans("0123856749", "0123456789")


def toi_number(number: int) -> int:
    """Translate a TOI 700 d number to Earth integer."""
    return int(str(number).translate(TOI_KEY))


numbers = sorted(tallista, key=toi_number)

print(f"Index 492: {numbers[492]}")
# Index 492: 5991
