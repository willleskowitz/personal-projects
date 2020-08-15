import random
import math


class Primes:
    @staticmethod
    def stream():
        '''My most recent attempt at creating a prime generator. This method
        uses a sieve that grows as the more primes are generated and removes
        unneeded entries to minimize memory use. This approach can generate
        a million primes in about 5 seconds.'''
        yield 2; yield 3; yield 5
        sieve = {9: 3, 25: 5}
        
        c = 7
        while True:
            if c not in sieve:
                sieve[c*c] = c; yield c
            else:
                p = sieve.pop(c)
                n = c + 2*p
                while n in sieve: n += 2*p
                sieve[n] = p
            c += 2    

    @staticmethod
    def stream2():
        ''' My second attempt at creating a prime generator. This method can
        generate a million primes in just under 25 seconds by utilizing the
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
    def stream3():
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
