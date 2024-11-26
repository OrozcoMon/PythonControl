llista=[] #llista buida
valor=int(input("Insereix un valor: ")) #insereixo el primer valor
maxim=0
while not valor == -1:
    llista.append(valor) #sumo el valor a la llista
    valor=int(input("Insereix un valor: ")) #vaig afegint valors
    print(llista) #print per comprovar si els valors s'afegeixen a la llista
    if valor > maxim:
        maxim=valor
        print(maxim)
#for maxim in range
