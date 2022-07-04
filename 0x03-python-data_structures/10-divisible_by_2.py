#!/usr/bin/python3
# 10-divisible_by_2.py
# Henock Yared


def diviisible_by_2(my_list=[]):
    """Find all multiples of 2 in a list."""
    for i in range(len(my_list)-1):
        new_list = [True if my_list[i] % 2 == 0 else False]
    return (new_list)
