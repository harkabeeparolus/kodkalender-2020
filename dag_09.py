#! /usr/bin/env python3

"""Unga programmerare kodkalender 2020, lucka 9"""
# https://ungaprogrammerare.se/kodkalender/lucka-9/

from input_files.dag_9_input import lista


def cookies_at_pos(pos):
    "Count the sum of cookies in the neighbors houses"
    left = lista[pos - 1] if pos > 0 else 0
    right = lista[pos + 1] if pos + 1 < len(lista) else 0
    return left + right


top_pos = max(range(len(lista)), key=cookies_at_pos)
top_cookies = cookies_at_pos(top_pos)

print(f"Position {top_pos}: {top_cookies} kakor")
# Position 185: 333 kakor
