#! /usr/bin/env python3

"""Unga programmerare kodkalender 2020, lucka 2."""
# https://ungaprogrammerare.se/kodkalender/lucka-2/

from input_files.dag_2_input import lista

buttons = {"u": 1, "n": -1}
floor_number = sum(buttons[x] for x in lista)

print(f"Våning: {floor_number}")
# Våning: 29
