llista = []
cadena = int(input("Nombre: "))
 
while cadena != -1:
    llista.append(cadena)
    cadena = int(input("Nombre: "))
print(llista)
 
n = float('-inf') #menys infinit=valor especial utilitzat per indicar un numero extremendament petit
for i in range(0,len(llista)): 
    if llista[i] > n: #al posar -inf qualsevol numero de la llista será major que n
        n = llista[i] #assegura que el primer valor assignat a la llista sempre será llista[i] > n
 
i = 0
llista_divisors = []
while i < len(llista):
    if n % llista[i] == 0:
        llista_divisors.append(llista[i])   
    i += 1
print("Número més gran: ",n," i els divisors: ",llista_divisors)
