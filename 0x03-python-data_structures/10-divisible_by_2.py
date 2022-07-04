#!/usr/bin/python3
# 10-divisible_by_2.py
# Henock Yared


def diviisible_by_2(my_list=[]):
    """Find all multiples of 2 in a list."""
    multiples = []
    for i in range(len(my_list)):
        multiples = [True if my_list[i] % 2 == 0 else False]
    
    return (multiples)
