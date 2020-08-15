import random
import math


class Primes:
    @staticmethod
    def stream():
        '''Prime generator. This method can generate a million primes in just 
        under 30 seconds by utilizing the Miller-Rabin primality test while
        skipping common composites. The k within the isprime function controls
        the accuracy of the Miller-Rabin primality test. The test will declare
        a composite as prime with a probability at most 4^−k. By default, k = 4.'''
        
        primes = [2, 3]
        
        yield 2
        yield 3
        
        def miller(n, d):
            a = random.randint(2, n - 1)
            x = pow(a, d, n)
            if x == 1 or x == n - 1: return True
            
            while d != n - 1:
                x = (x*x) % n
                d *= 2
                
                if x == 1: return False
                if x == n - 1: return True
                
            return False
        
        def isprime(n, k = 4):            
            if n % 2 == 0 or n == 3: return False
            
            d = n - 1; 
            while (d % 2 == 0): 
                d //= 2
                
            for _ in range(k):
                if miller(n, d) == False: return False
            
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
    def stream2():
        '''Slightly less efficient prime generator. This method can generate a
        million primes just under 33 seconds. This also utilizes the Miller-Rabin 
        primality test but does not optimize by skipping common composites.'''
        
        yield 2
        yield 3
        
        def miller(n, d):
            a = random.randint(2, n - 1)
            x = pow(a, d, n)
            if x == 1 or x == n - 1: return True
            
            while d != n - 1:
                x = (x*x) % n
                d *= 2
                
                if x == 1: return False
                if x == n - 1: return True
                
            return False
            
        
        def isprime(n, k = 4):
            
            if n % 2 == 0 or n == 3: return False
            
            d = n - 1; 
            while (d % 2 == 0): 
                d //= 2
                
            for _ in range(k):
                if miller(n, d) == False: return False
            
            return True
        
        n = 5
        while n < 30:
            if isprime(n):
                yield n
            n += 2
            
        k = 1
        while True:
            for i in (1, 7, 11, 13, 17, 19, 23, 29):
                n = 30*k + i

                if isprime(n):
                    yield n
            k += 1
            
    @staticmethod
    def stream3():
        '''Inefficient prime generator, though all primes produced are actually 
        primes, not probable primes.'''
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
            
    @staticmethod
    def sieve_of_eratosthenes(max_n):
        '''Implementation of the ancient Sieve of Eratosthenes, which will return all
        prime numbers up to max_n as a list.'''
        primes = [2] + list(range(3, max_n + 1, 2))
        i = 1
        while primes[i] < primes[-1]**0.5:
            [primes.remove(n) for n in range(primes[i]*2, primes[-1] + 1, primes[i]) if n in primes]
            i += 1
        
        return primes
