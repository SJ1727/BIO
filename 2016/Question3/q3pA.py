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
    i = 1
    while n - i > 0:
        surrounding.append(n - i)
        i <<= 1
    return surrounding

l, p, q = list(map(lambda x: int(x), input().split()))
primes = get_primes(l)

to_search = set([p])
searched = set()
i = 1
searching = True
while searching:
    new_l = set()
    for num in list(to_search):
        for surr in get_surrounding_pow_away(num, l):
            if surr == q:
                searching = False
            if surr in searched:
                continue
            if surr not in primes:
                continue
            new_l.add(surr)
    to_search = new_l
    i += 1

print(i)