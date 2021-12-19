"""
In questo esercizio si richiede di ritornare True se un dato numero n è primo, ovvero se non ha divisori al di fuori di sé stesso e 1.
Aspettarsi che l'input della funzione da definire sia già un numero intero n.
"""

# Esistono diversi approcci matematici

# 1. Naive
def controlla_primo_naive(n):
    if n < 2: return False
    for i in range(2, n):
        if (n%i)==0: return False
    return True

# 2. Ottimizzato
import math

def controlla_primo_meno_controlli(n):
    if n < 2: return False

    # Superata la radice quadrata (arrotondata) di n, non possiamo trovare più altri divisori
    limite = math.floor(math.sqrt(n))

    for i in range(2, limite):
        if (n%i)==0: return False
    return True

# 3. Crivello di Eratostene

N = 1001 # Supponiamo di voler filtrare i primi 1000 numeri positivi
crivello = [True for _ in range(N)]

# Porremo a False le posizioni relative a numeri non-primi

crivello[0] = False
crivello[1] = False # 0 e 1 non sono primi

p = 2
while (p * p < N):  # Fermati quando hai testato fino a sqrt(N)
    if crivello[p]: # Se il numero ha passato il setaccio:
        for i in range(p ** 2, N, p):   # Poni a false tutti i suoi multipli
            crivello[i] = False
    p += 1 # passa al prossimo numero


def controlla_primo_crivello(n):
    # Idea: alcuni dei numeri controllati come divisori sono esclusi in base a precedenti divisori.
    # Esempio: se 2 non divide n, non ha senso controllare se 4 o 6 o 8 dividono n
    # Implementazione: si tiene una lista dei numeri primi già incontrati e si usa come lista di controllo
    if n>=N: return controlla_primo_meno_controlli(n)
    return crivello[n] # La funzione si limita ad una banale ricerca in una lista pre-riempita

# Decidiamo qua quale delle tre definizioni usare
controlla_primo = controlla_primo_crivello

assert not controlla_primo(0)
assert not controlla_primo(1)
assert controlla_primo(11)
assert controlla_primo(13)

print("Se sei arrivato qui, congratulazioni!")