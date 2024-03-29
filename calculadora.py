def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b

if __name__ == "__main__":
    while True:
        print("Bienvenido a la calculadora")
        print("Seleccione la operación que desea realizar:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")

        opcion = input("Ingrese el número de la operación deseada: ")

        if opcion == "5":
            print("¡Hasta luego!")
            break

        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if opcion == "1":
            resultado = sumar(num1, num2)
            print("El resultado de la suma es:", resultado)
        elif opcion == "2":
            resultado = restar(num1, num2)
            print("El resultado de la resta es:", resultado)
        elif opcion == "3":
            resultado = multiplicar(num1, num2)
            print("El resultado de la multiplicación es:", resultado)
        elif opcion == "4":
            try:
                resultado = dividir(num1, num2)
                print("El resultado de la división es:", resultado)
            except ValueError as e:
                print("Error:", e)
        else:
            print("Opción no válida")
