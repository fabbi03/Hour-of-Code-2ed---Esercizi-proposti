"""
In questo esercizio si richiede di invertire un dato numero intero, es: 1234 diventa 4321.
Aspettarsi che l'input della funzione da definire sia già un numero intero n.
"""

# Esistono diversi approcci: si chiameranno "inverti_numero1" l'approccio naive, e "inverti_numero2" quello "Pythonico"

def inverti_numero1(n):
    # Per ogni cifra dall'ultima, aggiungila all'output e incrementalo di un posto
    num_cifre = len(str(n))

    inv = 0

    for _ in range(num_cifre):
        last_digit = n % 10 # ottieni ultima cifra
        inv = inv * 10 + last_digit # inserisci la cifra e aumenta di un posto
        n = n // 10 # elimina l'ultima cifra
    
    return inv

def inverti_numero2(n):
    # Trasforma il numero in una lista di cifre testuali, invertila, e ricomponi il numero
    lista_cifre = list(str(n))
    lista_cifre.reverse()
    risultato_testo = ""
    for cifra in lista_cifre:
        risultato_testo += cifra
    return int(risultato_testo)

# Decidiamo qua quale delle due definizioni usare
inverti_numero = inverti_numero2

assert inverti_numero(0) == 0
assert inverti_numero(1234) == 4321
assert inverti_numero(1200) == 21

print("Se sei arrivato qui, congratulazioni!")