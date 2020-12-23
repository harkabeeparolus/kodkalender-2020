#! /usr/bin/env python3

"""Unga programmerare kodkalender 2020, lucka 11"""
# https://ungaprogrammerare.se/kodkalender/lucka-11/

from input_files.dag_11_input import postnummer_lista


def postcode_is_ok(i: int) -> bool:
    "Validate a postcode"
    return "8" in str(i) and "1" not in str(i)


valid_postcodes = [n for n in postnummer_lista if postcode_is_ok(n)]

print(f"Antal postnummer: {len(valid_postcodes)}")
# Antal postnummer: 778
