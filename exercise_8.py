def run():
    num_1 = int(input("Ingrese un dividendo: "))
    num_2 = int(input ("Ingrese un divisor: "))
    cociente = num_1 // num_2
    resto = num_1 % num_2
    return print(f'el cociente es {cociente} y el resto es {resto}')



if __name__ == '__main__':
    run()