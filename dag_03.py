#! /usr/bin/env python3

"""Unga programmerare kodkalender 2020, lucka 3."""
# https://ungaprogrammerare.se/kodkalender/lucka-3/

import functools
import math
import operator

a = math.factorial(100)
b = functools.reduce(operator.mul, range(2, 165, 2))
how_many = round(a / b)

print(f"Antal delar: {how_many}")
# Antal delar: 40599194442
