#! /usr/bin/env python3

"""Unga programmerare kodkalender 2020, lucka 7."""
# https://ungaprogrammerare.se/kodkalender/lucka-7/

import itertools as it

from input_files.dag_7_input import talföljd

numbers = (int(digit) for digit in str(talföljd))
signs = it.chain([1], it.cycle([1, -1]))
password = sum(x * sign for x, sign in zip(numbers, signs))

print(f"Lösenord: {password}")
# Lösenord: 34
