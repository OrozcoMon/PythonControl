#En un control han registrat la seqüència de cotxes que han passat segons si són
#Gasolina(G), Diesel(D), Híbrids(H) o Elèctrics(E). Donada una cadena que conté
#G,D,H i E, convertir les G (Gasolina) per P(Petrol) (deixar en majúscules) 


print("entra la seqüència")
cadena=input()
cadena=cadena.upper()
cadena=cadena.replace("G","P")
print(cadena)
