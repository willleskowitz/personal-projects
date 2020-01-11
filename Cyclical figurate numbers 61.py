"""
Project Euler Problem 61
Cyclical figurate numbers
12/24/2019
"""

# Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers
# are all figurate (polygonal) numbers and are generated by the following 
# formulae:

# Triangle	 	P3,n = n(n+1)/2	 	1, 3, 6, 10, 15, ...
# Square	 	P4,n = n^2	 	    1, 4, 9, 16, 25, ...
# Pentagonal	P5,n = n(3n−1)/2	1, 5, 12, 22, 35, ...
# Hexagonal	 	P6,n = n(2n−1)	 	1, 6, 15, 28, 45, ...
# Heptagonal	P7,n = n(5n−3)/2	1, 7, 18, 34, 55, ...
# Octagonal	 	P8,n = n(3n−2)	 	1, 8, 21, 40, 65, ...
# The ordered set of three 4-digit numbers: 8128, 2882, 8281, has three 
# interesting properties.

# The set is cyclic, in that the last two digits of each number is the first
# two digits of the next number (including the last number with the first).
# Each polygonal type: triangle (P3,127 = 8128), square (P4,91 = 8281), and
# pentagonal (P5,44 = 2882), is represented by a different number in the set.
# This is the only set of 4-digit numbers with this property.
# Find the sum of the only ordered set of six cyclic 4-digit numbers for
# which each polygonal type: triangle, square, pentagonal, hexagonal, 
# heptagonal, and octagonal, is represented by a different number in the set.

import time

## POLYGONAL SET CREATION
def polygonal_sets(digits = 4):
    ''''Returns a list of sets of all triangle, square, pentagonal, hexagonal,
    heptagonal, and octagonal numbers with the specified digits.'''
    
    # Assign variables
    polygonals = []
    
    # Polygonal formulae 
    nth_triangle = lambda n: int(n * (n + 1) / 2)
    nth_square = lambda n: int(n * n)
    nth_pentagonal = lambda n: int(n * (3 * n - 1) / 2)
    nth_hexagonal = lambda n: int(n * (2 * n - 1))
    nth_heptagonal = lambda n: int(n * (5 * n - 3) / 2)
    nth_octagonal = lambda n: int(n * (3 * n - 2))
    
    formulae = [nth_triangle, nth_square, nth_pentagonal, nth_hexagonal, 
                nth_heptagonal, nth_octagonal]
    
    for formula in formulae:
        n = 1
        polygonal_set = set()
        
        while True:
            P = formula(n)
            if len(str(P)) > digits:
                break
            elif len(str(P)) == digits:
                polygonal_set.add(str(P))
                
            n += 1        
        
        polygonals.append(polygonal_set)
        
    return polygonals

## CONDITIONAL FUNCTIONS
# Order relevant
def cyclical_set(numbers):
    '''Returns True if the ordered set is cyclical and False otherwise.'''
    if type(numbers[0]) == int:
        numbers = [str(n) for n in numbers]
    for i in range(len(numbers)):
        if i == 0:
            if numbers[-1][2:] != numbers[i][:2]:
                return False
        else:
            if numbers[i - 1][2:] != numbers[i][:2]:
                return False
    return True

def cyclical_pair(pair):
    '''Returns True if the pair of numbers is cyclical and False otherwise.'''
    if type(pair[0]) == int:
        pair = [str(n) for n in pair]
    if pair[0][2:] == pair[1][:2]:
        return True
    return False


## SEARCH FUNCTION
def set_search(polygonals, cyclicals, indexes):
    '''Uses backtracking to search for the cyclical set of six four-digit polygonal 
    numbers.'''
    # Create leftover list to pull potential set members from
    leftovers = polygonals[:]
    
    try:
        for i in indexes:
            leftovers.remove(polygonals[i])
    except:
        pass
    
    # If length is 6, the set is complete
    if len(cyclicals) == 6:
        if cyclical_set(cyclicals):
            return True
        return False
    
    i = 0
    
    for subset in leftovers:
        
        # Ensure correct index 
        while i in indexes:
            i += 1
        
        for P in subset:
            try:
                is_cyclical = cyclical_pair([cyclicals[-1], P])
            except IndexError:
                is_cyclical = True
            
            if is_cyclical:
                
                # Append variables
                cyclicals.append(P)
                indexes.append(i)
                
                # Recursion 
                if set_search(polygonals, cyclicals, indexes):
                    return True
                
                # Backtrack
                cyclicals.remove(P)
                indexes.remove(i) 
                
        i += 1
       
    return False
                
def main():
    # Begin measuring elapsed time
    start = time.time()
        
    # Variable assignment for set_search   
    polygonals = polygonal_sets()
    cyclicals = []
    indexes = []

    # Call function
    set_search(polygonals, cyclicals, indexes)
    
    # Convert cyclical str to int for sum
    cyclicals = [int(n) for n in cyclicals]
    
    # Stop measuring elapsed time
    end = time.time()
    
    # Print results
    print('Ordered Set:', cyclicals)
    print('Sum:', sum(cyclicals))
    print('Execution time:', end - start)

if __name__ == '__main__':
    main()