# Hacer el diagrama de flujo y programa en Python, que lea números enteros y positivos(uno en cada lectura), y que averigue e imprima cuantos son pares y cuantos son impares. Para terminar utilizaremos el registro centinela para cuando el valor del número leído sea 0.



print("------------------------------------------")
print("-------Lectura de números positivos-------")
print("------------------------------------------")


# input

n = int(input("Digite el valor del número natural positivo que quiera evaluar: "))

# processing

cant_numeros_pares = 0
cant_numeros_impares = 0

while n != 0:
    if n%2 == 0:
        cant_numeros_pares = cant_numeros_pares + 1
    else:
        cant_numeros_impares = cant_numeros_impares + 1

    
    n = int(input("Digite el valor del número natural positivo que quiera evaluar: "))

#output

print("La cantidad de números pares es de " +str(cant_numeros_pares))
print("La cantidad de números impares es de "+str(cant_numeros_impares))
