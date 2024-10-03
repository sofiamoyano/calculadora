
def sumar():
    try:
        a = float(input("Ingrese el primer número para sumar: "))
        b = float(input("Ingrese el segundo número para sumar: "))
        resultado = a + b
        print(f"El resultado es: {resultado}")
    except ValueError:
        print("Error: Ingrese valores numéricos válidos.")

def restar():
        a = float(input("Ingrese el primer número para restar: "))
        b = float(input("Ingrese el segundo número para restar: "))
        resultado = a - b
        print(f"El resultado es: {resultado}")

def multiplicar():
        a = float(input("Ingrese el primer número para multiplicar: "))
        b = float(input("Ingrese el segundo número para multiplicar: "))
        resultado = a * b
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
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        sumar()
    elif opcion == "2":
        restar()
    elif opcion == "3":
        multiplicar()
    elif opcion == "4":
        dividir()
    else:
        print("Opción no válida")

menu()


