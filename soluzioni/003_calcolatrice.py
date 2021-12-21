"""
In questo esercizio si richiede di progettare una funzione che accetti una stringa rappresentante un'espressione (es. 42 * 3),
e ritorni il risultato atteso come numero.
Nel caso in cui l'espressione in input non sia valida, si ritorni un valore costante pari a None.
Aspettarsi che l'input della funzione da definire sia una stringa.
Dopo gli assert, si pone un loop di input utente per testare la funzione. Si inserisca un'espressione non valida per terminare il loop.
"""

import re

# Definiamo prima di tutto il pattern per decidere se la stringa è valida o meno.
pattern_float = "([+-])?\s*(([0-9]*[.])?[0-9]+)"
pattern = "\s*"+pattern_float+"\s*([+\-/\*xX])\s*"+pattern_float+"\s*"

# Python possiede una funzione, "eval", proprio allo scopo di tradurre un'espressione testuale in un'esecuzione effettiva di codice.
# Il problema di questa funzione è proprio quello di valutare QUALUNQUE stringa di testo, e quindi anche un'ipotetica funzione malevola.
# Creiamo quindi due versioni della funzione, una "unsafe" ed una "safe".

def calcolatrice_unsafe(expr):
    if re.match(pattern, expr)!=None:
        res = eval(expr)
        return res
    return None

def calcolatrice_safe(expr):
    match = re.search(pattern, expr)
    if match!=None and re.match(pattern, expr)!=None:

        sign1, num1, _, op, sign2, num2, _ = match.groups() # i.e. "+3.5*-4.5" -> ('+', '3.5', '3.', '*', '-', '4.5', '4.')

        num1 = float(num1)
        if sign1 == "-": num1 *= -1 # ottieni il primo operando, col segno

        num2 = float(num2)
        if sign2 == "-": num2 *= -1 # ottieni il secondo operando, col segno

        if op=="x" or op=="X": op="*"           # caso di "x" o "X" per moltiplicazione
        if num2 == 0.0 and op=="/": return None # caso divisione per zero

        res = eval(str(num1)+op+str(num2))  # usa "eval" su una stringa safe generata da noi
        return res
    return None


# Decidiamo qua quale delle due definizioni usare
calcolatrice = calcolatrice_safe

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