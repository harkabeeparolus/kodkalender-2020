#! /usr/bin/env python3

"""Unga programmerare kodkalender 2020, lucka 20"""
# https://ungaprogrammerare.se/kodkalender/lucka-20/

from input_files.dag_20_input import instruktioner

movement = {"w": -1j, "a": -1, "s": 1j, "d": 1}  # complex numbers

pos = sum(movement[key] for key in instruktioner)

x, y = int(pos.real), int(pos.imag)
x_dir = "västerut" if x < 0 else "österut"
y_dir = "söderut" if y > 0 else "norrut"

print(f"Position: {abs(x)} snäpp {x_dir}, {abs(y)} snäpp {y_dir}")
# Position: 2 snäpp västerut, 9, snäpp norrut
