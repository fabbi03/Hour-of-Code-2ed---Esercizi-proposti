"""
In questo esercizio si richiede di progettare una funzione che prenda due argomenti, la LUNGHEZZA di un lato e il NUMERO di lati,
calcolando in uscita PERIMETRO e AREA di un relativo poligono regolare.
Ritornare None nel caso di valori di input non validi.
Aspettarsi che l'input della funzione siano due interi.
Dopo gli assert, si pone un loop di input utente per testare la funzione. Si inserisca un'espressione non valida per terminare il loop.
"""

# Si dia una lettura alla pagina di Wikipedia: https://it.wikipedia.org/wiki/Apotema_(geometria)
# L'apotema è una misura specifica di ciascun poligono regolare che rappresenta il rapporto fra AREA e SEMIPERIMETRO.

# Otteniamo una lista di valori da usare per ogni numero di lati, sfruttando l'apotema o una sua funzione.

def poligono_regolare1(lunghezza, numero):
    if lunghezza <= 0 or numero < 3 or numero > 20 :   
        # Il poligono con meno lati ha 3 lati. Consideriamo l'apotema per lati da 3 a 20
        return None

    lista_fn = [0.289, 0.5, 0.688, 0.866, 1.038, 1.207, 1.374, 1.539, 1.703, 1.866, 2.029, 2.191, 2.352, 2.514, 2.675, 2.836, 2.996, 3.157 ]
    # Preso da Wikipedia, fn = apotema / lato, per n fra 3 e 20
    perimetro = lunghezza * numero
    # Area = (perimetro * apotema)/2 = (n * l * apotema)/2 = (n * l * l * fn)/2
    fn = lista_fn[numero-3]
    area = (numero * lunghezza**2 * fn)/2
    return perimetro, area

# In realtà, Wikipedia ci dà una definizione di fn per poterlo calcolare per qualunque numero di lati.
import math

def poligono_regolare2(lunghezza, numero):
    if lunghezza <= 0 or numero < 3 :   
        # Il poligono con meno lati ha 3 lati.
        return None
    
    perimetro = lunghezza * numero

    # fn = 1 / (2 * tan(PI, n))
    fn = 1 / (2 * math.tan(math.pi / numero))

    # Preso da Wikipedia, fn = apotema / lato, per n fra 3 e 20
    # Area = (perimetro * apotema)/2 = (n * l * apotema)/2 = (n * l * l * fn)/2
    area = (numero * lunghezza**2 * fn)/2

    # Cerchiamo di eliminare l'errore di rappresentazione
    area = round(area, 4)
    return perimetro, area

# Decidiamo qua quale delle due definizioni usare
poligono_regolare = poligono_regolare2

assert poligono_regolare(5, 4)[0]==20
assert poligono_regolare(5, 4)[1]==25
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