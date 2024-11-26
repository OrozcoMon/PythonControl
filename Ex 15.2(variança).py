contador = 0
llista = []

while contador != 10:
    voltatge = float(input("Introdueix un voltatge: "))
    llista.append(voltatge)
    contador += 1

mitjana = sum(llista) / len(llista)

suma_quadrats = sum((x-mitjana)**2 for x in llista)

variança = suma_quadrats / len(llista)

print(f"La variança dels voltatges és: {variança}.")
