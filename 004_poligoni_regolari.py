"""
In questo esercizio si richiede di progettare una funzione che prenda due argomenti, la LUNGHEZZA di un lato e il NUMERO di lati,
calcolando in uscita PERIMETRO e AREA di un relativo poligono regolare.
Ritornare None nel caso di valori di input non validi.
Aspettarsi che l'input della funzione siano due interi.
Dopo gli assert, si pone un loop di input utente per testare la funzione. Si inserisca un'espressione non valida per terminare il loop.
"""

# grazie a Wikipedia, possiamo calcolare il numero fisso per qualunque numero di lati.
import math

def poligono_regolare(lenght, number):
    if lenght <= 0 or number < 3 :
        return None
    
    perimetro = lenght * number

    # fn = 1 / (2 * tan(PI, n))
    fn = 1 / (2 * math.tan(math.pi / number))

    # fn = apotema / lato, per n fra 3 e 20
    # Area = (perimetro * apotema)/2 = (n * l * apotema)/2 = (n * l * l * fn)/2
    area = (number * lenght**2 * fn)/2

    # eliminare l'errore di rappresentazione
    area = round(area, 4)
    return perimetro, area

risultato = poligono_regolare

assert risultato(5, 4)[0]==20
assert risultato(5, 4)[1]==25
assert risultato(-1, 4)==None
assert risultato(5, 0)==None
assert risultato(0, 0)==None

print("Se sei arrivato qui, congratulazioni!\n\n")

while True:
    l = int(input("Lunghezza lato: "))
    n = int(input("Numero lati: "))
    res = poligono_regolare(l, n)
    if res==None:
        print("Espressione non valida, termino il programma.")
        break
    else:
        perimetro, area = res
        print("Perimetro:", perimetro, ", Area:", area, "\n\n")