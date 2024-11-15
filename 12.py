#Crear una llista a partir d’ una seqüència de valors d’entrada acabada en *.
#Una vegada creada, modificar-la elevant al quadrat tots els parells i al cub tots els
#senars, i mostrar-la. 


llista=[]
seq=input("Insereix un valor1: ")
while not seq=="*":
    seq=int(seq)                            #hacer conversión de lista a enter
    llista.append(seq)
    seq=input("Insereix un valor2: ")
    print(llista)
for i in range (0,len(llista)):
    if llista[i] % 2 == 0:
        llista[i]=llista[i]**2
    else:
        llista[i]=llista[i]**3
print(llista)
