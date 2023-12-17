# Prime number generator:

# it generates prime numbers from 2 to 1000
# Sieve of Erathostenes is an algorithm for finding all prime numbers up to any given limit



def sieve_of_eratosthenes(num: int) -> list:
    sieve = [True for i in range(num+1)]

    p = 2
    while (p*p <= num):
        if (sieve[p] == True):
            for i in range(p*p, num+1, p):
                sieve[i] = False
        p += 1

    for p in range(2, num+1):
        if sieve[p]:
            print(p)


# driver program
if __name__ == '__main__':
    num = 20
    print('\n')
    print(f'prime numbers up to {num} are: ')
    sieve_of_eratosthenes(num)
    print('\n')















if __name__ == '__main__':
    pass