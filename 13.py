#Eliminar el primer múltiple del darrer element d’una seqüència d’enters
#acabada en *

llista=[] #faig una llista buida
seq=input("Insereix un valor: ") #insereixo el primer valor
while not seq == "*": #mentres no sigui *
    seq=int(seq) #passo el valor a int
    llista.append(seq) #afegeixo el valor a la llista (funció append)
    seq=input("Insereix un valor: ") #insereixo els següents valors
    print(llista) #m'ensenya la llista que insereixo

ult_ele=llista[-1] #l'últim element és la llista menys 1
index=0 #el index és la posició dintre de una llista, comença en 0
while not (llista[index] % ult_ele == 0 or index == len(llista)-1): 
    index+=1 #faig un bucle sumant les posicions de l'índex

if index != len(llista)-1: 
    del llista [index] #borra el múltiple
    print(llista)
else:
    print(llista,"No hi ha")
