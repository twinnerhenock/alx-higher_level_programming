#!/usr/bin/python3
# 10-divisible_by_2.py
# Henock Yared


def diviisible_by_2(my_list=[]):
    """Find all multiples of 2 in a list."""
    my_list = [True for i in my_list if my_list[i] % 2 == 0 else False]
    return (my_list)
