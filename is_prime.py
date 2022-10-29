def is_prime(n):
    if n == 1 or n == 0:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 6   # jesli sprawdzilismy czy liczba dzieli sie przez 2 i 3 to wystarczy sprawdzac kolejne liczby +1 -1 od 6, bo tylko to sa kandydaci na liczby 1
    while (i-1)**2 <= n+1:
        if n % (i-1) == 0 or n % (i+1) == 0:
            return False
        i += 6
    return True
