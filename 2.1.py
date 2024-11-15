#Els moviments que realitza un braç robot estan codificats amb L,R,U i D. Ens entren
#una seqüència de moviments i volem saber si més de la meitat són U.
#mi versión


cadena=input("Insereix la seqüència: ")
cadena=cadena.upper()
cadenaU=cadena.count("U")
cadena=len(cadena)
if cadenaU > cadena / 2:
    print("Hi ha més de la meitat", cadenaU)
else:
    print("No hi ha més de la mitad", cadenaU)
