#! /usr/bin/env python3

"""Unga programmerare kodkalender 2020, lucka 20"""
# https://ungaprogrammerare.se/kodkalender/lucka-20/

from input_files.dag_20_input import instruktioner

movement = {"w": -1j, "a": -1, "s": 1j, "d": 1}  # complex numbers

pos = sum(movement[key] for key in instruktioner)

x, y = int(pos.real), int(pos.imag)
x_dir = "österut" if x > 0 else "västerut"
y_dir = "norrut" if y < 0 else "söderut"
x, y = abs(x), abs(y)

print(f"Position: {x} snäpp {x_dir}, {y}, snäpp {y_dir}")
# Position: 2 snäpp västerut, 9, snäpp norrut
