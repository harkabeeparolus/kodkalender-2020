#! /usr/bin/env python3

"""Unga programmerare kodkalender 2020, lucka 9"""
# https://ungaprogrammerare.se/kodkalender/lucka-9/

from dag_9_input import lista

length = len(lista)
top_cookies = 0
top_pos = None

for i in range(length):
    left = lista[i - 1] if i > 0 else 0
    right = lista[i + 1] if i + 1 < length else 0
    cookies = left + right
    if cookies > top_cookies:
        top_cookies = cookies
        top_pos = i

print(f"Position {top_pos}: {top_cookies} kakor")
# Position 185: 333 kakor
