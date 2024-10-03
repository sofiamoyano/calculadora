def sumar():
        a = float(input("Ingrese el primer número para sumar: "))
        b = float(input("Ingrese el segundo número para sumar: "))
        resultado = a + b
        print(f"El resultado es: {resultado}")


def dividir():
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))   
        # Verificar que el divisor no sea cero
        if b == 0:
            print("Error: No se puede dividir entre 0.")
        else:
            resultado = a / b
            print(f"El resultado es: {resultado}")

def menu():
    print("1. Sumar")
    print("2. Dividir")
    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        sumar()
    elif opcion == "2":
        dividir()
    else:
        print("Opción no válida")

menu()

