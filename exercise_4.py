def coste_por_hora(horas,costo):
    horas = int(horas)
    costo = int(costo)
    return print(f'el costo de las horas trabajadas es de {horas*costo}')

print(
    """
    Calculador De Precio por Hora trabajada

    """
)
costo = input("Cuando le pagan por hora: ")
horas = input("Cuantas Horas trabaja: ")

assert costo.isnumeric() and horas.isnumeric(), 'Ingrese un numero'

print(coste_por_hora(horas,costo))