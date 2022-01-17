"""
In questo esercizio si richiede di ritornare True se un dato numero n è primo, ovvero se non ha divisori al di fuori di sé stesso e 1.
Aspettarsi che l'input della funzione da definire sia già un numero intero n.
"""

def controlla_primo_naive(n):
    if n < 2: return False
    for i in range(2, int(n/2)+1):
        if (n%i)==0: return False
    return True

assert not controlla_primo_naive(0)
assert not controlla_primo_naive(1)
assert controlla_primo_naive(11)
assert controlla_primo_naive(13)

print("Se sei arrivato qui, congratulazioni!")