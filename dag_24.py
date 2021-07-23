#! /usr/bin/env python3

"""Unga programmerare kodkalender 2020, lucka 24."""
# https://ungaprogrammerare.se/kodkalender/lucka-24/

from input_files.dag_24_input import nissar

transform = {"<": ">", ">": "<", "^": "^"}
new_queue = "".join(transform[nisse] for nisse in nissar)
turned = 2 * new_queue.count("<>")  # 2 characters per match

print(f"Nissar som pratar: {turned}")
# Nissar som pratar: 510
