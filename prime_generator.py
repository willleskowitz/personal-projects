import random
import math
from itertools import count, cycle, compress


class Primes:
    @staticmethod
    def stream_v4():
        '''Efficient prime generator. This method uses a sieve that
        grows as the more primes are generated and removes unneeded entries
        to minimize memory use. This approach can generate a million primes
        in around 3.2 seconds on my machine.
        
        
        This function is based off a submission by user tzot from StackOverflow,
        with some minor changes. First, mod was a hardcoded frozenset of integers. Albeit
        this is more efficient, but it fails to explain the rationale behind it.
        This part of the code is exploiting the fact that all primes above 30
        (2*3*5) can be written in the form 30*k + i where k is a natural number 
        and 1<i<30 such that gcd(i,30) = 1. Representing primes this way increases
        generation efficiency by avoiding multiples of 2, 3, and 5.
        
        Second, skip was a hardcoded tuple of fifteen 1's and 0's for the cycle function.
        Instead, I included a list comprehension representing the logic of this 
        variable. For a prime p where p >= 7, p % 30 = i such that gcd(i,30) = 1. 
        This becomes evident when reviewing the representation p = 30*k + i.
        Therefore, any numbers not in this format can be skipped. Hence, skip
        represents this in a format thecycle function can read to filter these
        cases. This can be cycled since i remains the same as k increases.
        
        Lastly, the entries {9: 3, 25: 5} were removed from the sieve as they would
        never be use since the filter skips multiples of 3's and 5's as mentioned above.
        
        Any other changes made were for readability. I hope you find this useful!'''

        yield 2; yield 3; yield 5
        sieve = {}
        start = 7
        base = 2*3*5
        mod = [i for i in range(base) if math.gcd(i, base) == 1]
        skip = tuple([1 if n % base in mod else 0 for n in range(start, base + start, 2)])
        mod = frozenset(mod)

        for c in compress(count(start, 2), cycle(skip)):
            if c not in sieve:
                sieve[c*c] = c; yield c
            else:
                p = sieve.pop(c)
                n = c + 2*p
                while n in sieve or n % base not in mod: n += 2*p
                sieve[n] = p
    
    @staticmethod
    def stream_v3():
        '''This prime generator uses a similar algorithm as stream_v4, though
        with base 210 (2*3*5*7) rather than base 30 (2*3*5). My hunch was that
        this approach would be an improvement since multiples of 7 would be 
        skipped, though I was wrong. I included the function mostly because
        of its novelty. It can produce a million primes in 6.38 seconds.''' 
        
        start = 31; base = 210
        initial_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
        for prime in initial_primes:
            yield prime

        sieve = {49: 7, 121: 11, 169: 13, 289: 17, 361: 19, 529: 23, 841: 29, 961: 31}

        mod = [i for i in range(base) if math.gcd(i, base) == 1]
        skip = [1 if n % base in mod else 0 for n in range(start, start + base, 2)]

        for c in compress(count(start, 2), cycle(skip)):
            if c not in sieve:
                sieve[c*c] = c; yield c
            else:
                p = sieve.pop(c)
                n = c + 2*p
                while n in sieve or n % base not in mod: n += 2*p
                sieve[n] = p

    @staticmethod
    def stream_v2():
        ''' My second attempt at creating a prime generator. This method can
        generate a million primes in ~25 seconds by utilizing the
        Miller-Rabin primality test while skipping common composites. The k 
        within the isprime function controls the accuracy of the Miller-Rabin 
        primality test. The test will declare a composite as prime with a 
        probability at most 4^−k. By default, k = 3.'''
        
        primes = [2, 3]
        
        yield 2
        yield 3
        
        def isprime(n, k = 3):
            r = 0
            d = n - 1
            while d % 2 == 0:
                r += 1
                d //= 2
            
            for _ in range(k):
                a = random.randint(2, n - 1)
                x = pow(a, d, n)
                
                if x == 1 or x == n - 1: continue
            
                cont = False
                for _ in range(r - 1):
                    x = pow(x, 2, n)
                    if x == n - 1: cont = True; break
                
                if cont: continue
                
                return False
            
            return True
        
        n = 5
        while n < 30:
            if isprime(n):
                primes.append(n)
                yield n
            n += 2
        
        i = 2
        base = 2*3*5
        last_n = 0
        
        while True:   
            next_base = base * primes[i + 1]
            qs = [m for m in range(base) if math.gcd(m, base) == 1]
            k = 1
            
            while n < next_base:
                for q in qs:
                    n = base*k + q
                    
                    if last_n >= n: continue
    
                    if isprime(n):
                        yield n
                k += 1
                
            last_n = n
            i += 1
            base = next_base
            
    @staticmethod
    def stream_v1():
        '''My first, and least efficient, attempt at creating an
        infinite prime generator.'''
        primes = [2, 3]

        yield 2
        yield 3

        def isprime(n, primes):
            for prime in primes:
                if n % prime == 0:
                    return False
                if prime > n**0.5:
                    break

            return True


        n = 5
        while n < 30:
            if isprime(n, primes):
                primes.append(n)
                yield n
            n += 2

        k = 1
        while True:
            for i in (1, 7, 11, 13, 17, 19, 23, 29):
                n = 30*k + i

                if isprime(n, primes):
                    primes.append(n)
                    yield n
            k += 1
