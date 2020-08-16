import random
import math
from itertools import count, cycle, compress


class Primes:
    @staticmethod
    def stream_v3():
        '''Efficient prime generator. This method uses a sieve that
        grows as the more primes are generated and removes unneeded entries
        to minimize memory use. This approach can generate a million primes
        in 2.9 seconds on my machine.
        
        This function is based off a submission by user tzot from StackOverflow,
        with some of my own meaningful improvements to further improve efficiency.
        The original function exploited the fact that all primes above 5 can be
        written in the form p = c*k + i (c = 30 = 2*3*5) where k is a nonnegative
        integer and 0<i<c such that gcd(i, c) = 1. Representing primes this way 
        increases generation efficiency by avoiding multiples of 2, 3, and 5.
        
        Conveniently, more multiples can be avoided by increasing the constant c.
        If c = 2*3*5*7 = 210, all multiples of 7 can be avoided.
        Furthermore, if c = 2*3*5*7*11, all multiples of 11 can be avoided,
        and so on. The form p = c*k + i such that 0<i<c and gcd(i, c) = 1 holds
        true. Note that primes that are a factor of c cannot be represented
        this way.
        
        I implemented this fact into the algorithm to improve generation
        speeds. The sweet spot for generating a million primes seems to be
        with c = 2310, though different generation goals may benefit
        from different c values. I hope you find this useful!'''
        
        start = 13
        c = 2*3*5*7*11
        yield 2; yield 3; yield 5; yield 7; yield 11

        sieve = {}

        mod = [i for i in range(c) if math.gcd(i, c) == 1]
        skip = tuple([1 if n % c in mod else 0 for n in range(start, start + c, 2)])
        mod = frozenset(mod)

        for n in compress(count(start, 2), cycle(skip)):
            if n not in sieve:
                sieve[n*n] = n; yield n
            else:
                p = sieve.pop(n)
                m = n + 2*p
                while m in sieve or m % c not in mod: m += 2*p
                sieve[m] = p

    @staticmethod
    def stream_v2():
        '''My second attempt at creating a prime generator. This method can
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
