#! /usr/bin/env python3

"""Unga programmerare kodkalender 2020, lucka 16."""
# https://ungaprogrammerare.se/kodkalender/lucka-16/

from collections import Counter

from input_files.dag_16_input import julkulor

time_per_color = {"g": 1.25, "r": 1.5, "b": 1, "l": 1}

paint_times = [
    (amount * time_per_color[color], color)
    for color, amount in Counter(julkulor).items()
]

for hours, color in sorted(paint_times):
    print(f"Färg {color} tar {hours} timmar")

# Färg l tar 21 timmar
# Färg g tar 21.25 timmar
# Färg b tar 25 timmar
# Färg r tar 25.5 timmar
