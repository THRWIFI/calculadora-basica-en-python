# Solicita al usuario que ingrese los dos números
#primer numero
a = int(input("Ingrese el primer número: "))
#segundo numero
b = int(input("Ingrese el segundo número: "))

# Solicita al usuario que ingrese la operación a realizar
#como suma resta multiplicacion y division
operacion = input("Ingrese la operación a realizar (+, -, *, /): ")

# Verifica qué operación se seleccionó y realiza la operación correspondiente
#suma
if operacion == "+":
    #realiza la operacion
    resultado = a + b
    #muestra el resultado
    print("El resultado de la suma de", a, "y", b, "es:", resultado)
#resta
elif operacion == "-":
    #realiza la operacion
    resultado = a - b
    #muestra el resultado
    print("El resultado de la resta de", a, "y", b, "es:", resultado)
#multiplicacion
elif operacion == "*":
    #realiza la operacion
    resultado = a * b
    #Muestra el resultado
    print("El resultado de la multiplicación de", a, "por", b, "es:", resultado)
#division
elif operacion == "/":
    #realiza la operacion
    resultado = a / b
    #muestra el resultado
    print("El resultado de la división de", a, "por", b, "es:", resultado)
    #mensaje de error
else:
    # Si se ingresa una operación inválida, muestra un mensaje de error
    print("Operación inválida. Por favor ingrese una operación válida (+, -, *, /).")

# Imprime el resultado en la pantalla
if resultado:
    print("El resultado de la operación es:", resultado)
