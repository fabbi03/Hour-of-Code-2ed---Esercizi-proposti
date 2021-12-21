"""
In questo esercizio si richiede di invertire un dato numero intero, es: 1234 diventa 4321.
Aspettarsi che l'input della funzione da definire sia già un numero intero n.
"""

def inverti_numero(n):
    if not str(n).isdigit:
        return None
    return int( str(n)[::-1] )


assert inverti_numero(0) == 0
assert inverti_numero(1234) == 4321
assert inverti_numero(1200) == 21

print("Se sei arrivato qui, congratulazioni!")