def get_primes(n):
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return tuple([2] + [i for i in range(3,n,2) if sieve[i]])

def get_surrounding_pow_away(n, limit):
    surrounding = []
    i = 1
    while n + i < limit:
        surrounding.append(n + i)
        i <<= 1
    return surrounding

primes = get_primes(250_000)
count = 0
for i, prime in enumerate(primes):
    for surr in get_surrounding_pow_away(prime, 250_000):
        if surr in primes:
            count += 1
    if i % 100 == 0:
        print(prime)
print(count)