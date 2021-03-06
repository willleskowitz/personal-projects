"""
# Name:         Will Leskowitz
# Project:      Personal Projects
# Script:       multiply_to_n
# Date:         Wed Jul 29 17:26:57 2020
#
"""

from functools import reduce
from numpy import prod

def factors_of_n(n):
    '''Returns set of all factors of n.'''
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def multiply(n, k):
    '''Given a positive integer n, returns all possible ways k positive integers can multiply to give n as set of tuples.'''
    if k == 1: return {n}
    
    factors = factors_of_n(n)    
    l = [[item] for item in sorted(factors)]
    
    for i in range(k - 1):
        new_l = []
        for sublist in l:
            product = prod(sublist)
            if i == k - 2:
                for subfactor in factors_of_n(n//product):
                    if prod(sublist + [subfactor]) == n:
                        new_l.append(sublist + [subfactor])
            else:
                for subfactor in factors_of_n(n//product):
                    new_l.append(sublist + [subfactor])
                
        l = new_l
    
    return set([tuple(ele) for ele in l]) 
