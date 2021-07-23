#! /usr/bin/env python3

"""Unga programmerare kodkalender 2020, lucka 18."""
# https://ungaprogrammerare.se/kodkalender/lucka-18/

from input_files.dag_18_input import tallista


def is_palindrome(number: int) -> bool:
    """Test if a number is a palindrome."""
    as_string = str(number)
    return as_string == as_string[::-1]


palindromes = [n for n in tallista if is_palindrome(n)]

print(*palindromes, sep=", ")
print(f"Antal palindrom: {len(palindromes)}")

# 34743, 29392, 72627
# Antal palindrom: 3
