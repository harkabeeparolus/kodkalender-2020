#! /usr/bin/env python3

"""Unga programmerare kodkalender 2020, lucka 12"""
# https://ungaprogrammerare.se/kodkalender/lucka-12/

from input_files.dag_12_input import tallista


def collatz(number: int) -> int:
    "Collatz Problem"
    count = 0
    while number > 1:
        if number % 2:
            number = number * 3 + 1  # odd
        else:
            number //= 2  # even
        count += 1
    return count


winner = sum(collatz(n) for n in tallista)

print(f"Vinstlott: {winner}")
# Vinstlott: 1337
