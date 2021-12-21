"""
In questo esercizio si richiede di progettare una funzione che accetti una stringa rappresentante un'espressione (es. 42 * 3),
e ritorni il risultato atteso come numero.
Nel caso in cui l'espressione in input non sia valida, si ritorni un valore costante pari a None.
Aspettarsi che l'input della funzione da definire sia una stringa.
Dopo gli assert, si pone un loop di input utente per testare la funzione. Si inserisca un'espressione non valida per terminare il loop.
"""

def calcolatrice(expr):
    pass

assert calcolatrice("2+2")==4
assert calcolatrice("  30   *   2")==60
assert calcolatrice("ciao mondo 40*2")==None
assert calcolatrice("50/0")==None
assert calcolatrice("6/2")==3.0

print("Se sei arrivato qui, congratulazioni!\n\n")

while True:
    x = input("Inserisci la tua espressione: ")
    res = calcolatrice(x)
    if res==None:
        print("Espressione non valida, termino il programma.")
        break
    else:
        print("Risultato:", res, "\n\n")