#!/usr/bin/python3
# 1-number_of_lines.py
# Henock
"""Defines a text file line-counting function."""


def write_file(filename="", text=""):
    """Return the number of lines in a text file."""
    s = str(text)
    with open(filename) as f:
        f.write(s)
