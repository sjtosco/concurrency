import concurrent.futures
import math
import time

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]
PRIMES1 = [
    11,
    11,
    112,
    1,
    11,
    109]

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    s = time.time()
    #with concurrent.futures.ThreadPoolExecutor() as executor:
    for number, prime in zip(PRIMES, map(is_prime, PRIMES)):
        print('%d is prime: %s' % (number, prime))
    print("Elapsed time: %.2f"%(round(time.time()-s, 2)))

if __name__ == '__main__':
    main()
