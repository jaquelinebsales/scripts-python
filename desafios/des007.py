lista = []
for i in range(2):
    lista.append(float(input(f"Digite a {i+1}° nota: ")))


print(f"A média é {(lista[0] + lista[1])/2}")