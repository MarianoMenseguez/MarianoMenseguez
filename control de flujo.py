# 1) Realiza un programa que lea dos números por teclado y permita elegir entre 3 opciones en un menú:

# Mostrar una suma de los dos números
# Mostrar una resta de los dos números (el primero menos el segundo)
# Mostrar una multiplicación de los dos números
# En caso de no introducir una opción válida, el programa informará de que no es correcta.

n1 = float(input("Introduce un numero: "))
n2 = float(input("Introduce otro numero: "))
print("Que quieres hacer?")
print("1- SUMAR 2 NUMERO")
print("2- RESTAR LOS 2 NUMERO")
print("3- MUTIPLICAR LOS 2 NUMEROS")

opcion = input("Introduce una opcion: ")

if opcion == "1":
    print("la suma de ",n1, " + ",n2," es igual a ",(n1+n2) )
elif opcion == "2":
    print("la resta de ",n1, " - ",n2," es igual a ",(n1-n2) )
elif opcion == "3":
    print("la multiplicacion de ",n1, " * ",n2," es igual a ",(n1*n2) )    
else:
    print("La opcion es incorrecta")


# 2) Realiza un programa que lea un número impar por teclado. 
# Si el usuario no introduce un número impar, debe repetise el proceso hasta que lo introduzca correctamente.   

numero = 0

while numero % 2 == 0:
    numero = int(input("introduce un numero impar"))
  
  
#   3) Realiza un programa que sume todos los números enteros pares desde el 0 hasta el 100:

# list(range (0,101,2 ))
suma = sum(range(0,101,2))
print(suma)

# 4) Realiza un programa que pida al usuario cuantos números quiere introducir.
# Luego lee todos los números y realiza una media aritmética:

numeros = int(input("Cuantos numeros quieres introducir"))
suma = 0

for x in range(numeros):
    suma +=float(input("intrduce un numero: "))

print("se han introducido", numeros, "que en total suman", suma,"y la media es", suma/numeros)

# 6) Utilizando la función range() y la conversión a listas genera las siguientes listas dinámicamente:
print(list(range(0,11)))
print(list(range(-10,1)))
print(list(range(0,21,2)))
print(list(range(-19,0,2)))
print(list(range(0,51,5)))

# 7) Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas, 
# pero no debe repetise ningún elemento en la nueva lista:

lista_1= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_2= [0, 5, "chau", 3, "Hola", 6, 7, 10]
lista_3=[]
for letra in lista_1:
    if letra in lista_2 and letra not in lista_3:
        lista_3.append(letra)
print(lista_3) 