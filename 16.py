# Lista para almacenar los números de la serie
llista = []
 
# Entrada de números hasta que el usuario ingrese -1
valor = int(input("Dame una serie de números acabados en -1: "))
 
while not valor == -1:
    llista.append(valor)
    valor = int(input("Dame una serie de números acabados en -1: "))
 
# Encontramos el número más grande en la lista
num_max = max(llista)
 
# Encontramos los divisores del número más grande      
div = []
 
for num in llista:
    if num_max % num == 0:
        div.append(num)
 
# Mostrar el resultado
print(f"El número más grande es: {num_max}")
print(f"Los divisores que se encuentran en la serie son: {', '.join(map(str, div))}")
