#1. Escribe un script que imprima las primeras estrofas de la canción de la víbora de la mar con el siguiente formato:

# A la víbora, víbora
# 	De la mar, de la mar
# 		Por aquí pueden pasar
# 	Los de adelante corren mucho
# 		Y los de atrás se quedarán

# A la víbora, víbora
# 	De la mar, de la mar
# 		Por aquí pueden pasar
# 	Los de adelante corren mucho
# 		Y los de atrás se quedarán
# 		Tras, tras, tras

estrofa = "A la víbora, víbora \n \t De la mar, de la mar \n \t\t Por aquí pueden pasar \n \t Los de adelante corren mucho \n \t\t Y los de atrás se quedarán"
print(estrofa, "\n\n", estrofa, "\n \t\t Tras, tras, tras" ) 
print()

print("2. Escribe un programa que solicite el nombre, el apellido y la edad del usuario e imprima un saludo y su año de nacimiento. Tomar el año actual como constante (2023)")

nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = int(input("Ingresa tu edad: "))
año = 2023
año_de_nacimiento = año - edad
print("Hola " + nombre + " " + apellido + " " +"naciste en el año ", año_de_nacimiento ) 
print()

print("3. Escribe un script que calcule el área de un círculo basado en el radio proporcionado por el usuario e imprima el resultado.")
PI = 3.14159
radio = float(input("Proporciona el radio del círculo: "))
resultado = (PI * radio) ** 2
print("El área del círculo es:", resultado)
print()

print("4. Escribe un script que solicite un número (n) y calcule el valor de n + nn + nnn")
n = int(input("Introduce un numero entero :"))
resultado_1 = n + 2*n + 3*n
print("El valor final es:", resultado_1)
print()

print("5. Escribe un script que solicite un número y devuelva notifique al usuario si el número es par o impar") 
par_o_impar = int(input("Introduce un numero"))
if par_o_impar % 2 == 0:
  print("El numero qie ingresaste es par")
else:
  print("El numero que ingresaste es impar")  
print()

print("6. Escribe un script que solicite la base y la altura de un triángulo, calcule su área e imprima el resultado")

base = float(input("Ingresa la base de un triángulo: "))
altura = float(input("Ingresa la alura dek triángulo: "))
formula = (base * altura) / 2
print("El area del triangulo que ingresaste es: ", formula )













