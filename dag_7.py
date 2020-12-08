#! /usr/bin/env python3

"""Unga programmerare kodkalender 2020, lucka 7"""
# https://ungaprogrammerare.se/kodkalender/lucka-7/

from itertools import chain, cycle

from dag_7_input import talföljd


def varannan(seq):
    signs = chain([1], cycle([1, -1]))
    for number, sign in zip(seq, signs):
        yield number * sign


password = sum(varannan(int(x) for x in str(talföljd)))

print(f"Lösenord: {password}")
# Lösenord: 34
