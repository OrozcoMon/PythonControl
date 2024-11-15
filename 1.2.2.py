#Els moviments que realitza un braç robot estan codificats amb L,R,U i D. Ens entren
#una seqüència de moviments i volem saber si més de la meitat són U.
#versión joel


Codi=input("Se introducen codigos de movimiento: ")
Codi=Codi.upper()
CodiU=Codi.count("U")
CodiL=Codi.count("L")
CodiR=Codi.count("R")
CodiD=Codi.count("D")
print(CodiU)
if CodiU > ((CodiL+CodiR+CodiD+CodiU)/2):
    print("Hay mas de la mitad de 'U'")
else:
    print("Hay menos de la mitad")
