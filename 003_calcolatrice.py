"""
In questo esercizio si richiede di progettare una funzione che accetti una stringa rappresentante un'espressione (es. 42 * 3),
e ritorni il risultato atteso come numero.
Nel caso in cui l'espressione in input non sia valida, si ritorni un valore costante pari a None.
Aspettarsi che l'input della funzione da definire sia una stringa.
Dopo gli assert, si pone un loop di input utente per testare la funzione. Si inserisca un'espressione non valida per terminare il loop.
"""

import re

pattern_float = "([+-])?\s*(([0-9]*[.])?[0-9]+)"
pattern = "\s*"+pattern_float+"\s*([+\-/\*xX])\s*"+pattern_float+"\s*"

# funzione "eval"

#versione sbagliata della funzione
def calcolatrice_wrong(expr):
    if re.match(pattern, expr)!=None:
        res = eval(expr)
        return res
    return None

#versione giusta della fnzione
def calcolatrice_right(expr):
    match = re.search(pattern, expr)
    if match!=None and re.match(pattern, expr)!=None:

        sign1, num1, _, op, sign2, num2, _ = match.groups()

        num1 = float(num1)
        if sign1 == "-": num1 *= -1 

        num2 = float(num2)
        if sign2 == "-": num2 *= -1 

        if op=="x" or op=="X": op="*"           
        if num2 == 0.0 and op=="/": return None 

        res = eval(str(num1)+op+str(num2)) 
        return res
    return None


calcolatrice = calcolatrice_right

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