def peso_payaso(num):
    payaso = num * 112
    
    return payaso

def peso_muñecas(num):
    muñeca = num * 75

    return muñeca

def peso_juguetes(num):
    payaso = num * 112
    muñeca = num * 75

    return payaso + muñeca
    

def run():
    print(
        """
        Calcula el peso de los payasos y muñecas vendidos
        """
    )

    num = int(input("Cuantos juguetes se vendieron hoy?: "))
    print(f'Las {num} unidades vendidas en total pesaron {peso_juguetes(num)} gramos, los payasos pesaron {peso_payaso(num)} gr y las muñecas {peso_muñecas(num)} gr  ')

if __name__ == '__main__':
    run()