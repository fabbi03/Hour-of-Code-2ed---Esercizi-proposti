"""
In questo esercizio si richiede di progettare una funzione che prenda due argomenti, la LUNGHEZZA di un lato e il NUMERO di lati,
calcolando in uscita PERIMETRO e AREA di un relativo poligono regolare.
Ritornare None nel caso di valori di input non validi.
Aspettarsi che l'input della funzione siano due interi.
Dopo gli assert, si pone un loop di input utente per testare la funzione. Si inserisca un'espressione non valida per terminare il loop.
"""

def poligono_regolare(lunghezza, numero):
    pass

assert poligono_regolare(5, 4)==25
assert poligono_regolare(-1, 4)==None
assert poligono_regolare(5, 0)==None
assert poligono_regolare(0, 0)==None

print("Se sei arrivato qui, congratulazioni!\n\n")

while True:
    l = int(input("Quanto è lungo il lato: "))
    n = int(input("Quanti lati ci sono: "))
    res = poligono_regolare(l, n)
    if res==None:
        print("Espressione non valida, termino il programma.")
        break
    else:
        perimetro, area = res
        print("Perimetro:", perimetro, ", Area:", area, "\n\n")