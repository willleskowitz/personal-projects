class Primes:
    @staticmethod
    def stream():
        
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
            
        
        def isprime(n):
            k = 4
            
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
        def stream2():
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
