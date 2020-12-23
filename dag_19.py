#! /usr/bin/env python3

"""Unga programmerare kodkalender 2020, lucka 19"""
# https://ungaprogrammerare.se/kodkalender/lucka-19/

from input_files.dag_19_input import tallista

position = 0
for i in tallista:
    position = int(str(i)[position])

print(f"Nisse nummer: {position}")
# Nisse nummer: 4
