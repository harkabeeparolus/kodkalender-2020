#! /usr/bin/env python3

"""Unga programmerare kodkalender 2020, lucka 5"""
# https://ungaprogrammerare.se/kodkalender/lucka-5/

numbers_sum = sum(x for x in range(10_000, 100_001) if x % 3767 == 0)
continents = len(str(numbers_sum))

print(f"Antal världsdelar: {continents}")
# Antal världsdelar: 7
