# Definir el tamaño del vector
def llenarPolF1(n):
    # Crear un vector vacío
    print("Ingrese")
    polF1 = []
    for i in range(n):
        polF1.append(0.0)
    # Llenar el polinomio con valores ingresados por el usuario
    sw = 1
    while(sw):
        i = int (input("Ingrese el exponente del termino "))
        valor = float(input("Ingrese el  coeficiente para el exponente{}: ".format(i)))
        polF1[i] = valor
        sw = bool(int(input("Desea ingresar otro termino? 1: Si, 0: No")))

    return polF1


#PROGRAMA PRINCIPAL

n = int(input("Ingrese el tamaño máximo del polinomio: "))
polF1 = llenarPolF1(n)
print("El polinomio es:", polF1)