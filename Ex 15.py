#Ens donen per teclat una seqüència de 10 mesures de voltatge. Es demana que es calculi la
#variança associada a les mesures

compt_volt=0
llista=[]
while not compt_volt == 10:
    volt=float(input("Insereix un voltatge: "))
    llista.append(volt)
    compt_volt+=1
    print(llista)


#FALTA LA VARIANÇA NO LA FARÉ
