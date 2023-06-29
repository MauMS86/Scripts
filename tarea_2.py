# 1. Escribe un script que le pregunte al usuario varios nombres hasta que el usuario especifique que ya no desea ingresar más nombres.
#     Como resultado deberá mostrar al usuario una lista, una tupla y un set con todos los nombres que ingresó el usuario

lista_nombres= []
nombre = input("Escribe un nombre: ")
lista_nombres.append(nombre)
continuar = input("Deseas continuar?: Y / N ").lower()

while continuar == "y":
    nombre = input("Escribe otro nombre: ")
    lista_nombres.append(nombre)
    continuar = input("Deseas continuar?: Y / N ").lower()

    while continuar != "y" and continuar != "n":
        print("esa no es una opción valida. Escribe Y para continuar, N para parar.: ")
        continuar = input("Deseas continuar?: Y / N ").lower()

if continuar == "n":
    print("El programa ha finalizado")
    
print("Esta es una Lista: ", lista_nombres)
print("Esta es una Tupla: ", tuple(lista_nombres))
print("Este es un Set: ", set(lista_nombres))


# 2. Escribe un script que calcule la diferencia entre un número dado y 17 e imprima el resultado.
#     Si el número es más grande que 17 deberá imprimir el doble de la diferencia entre ambos números

numero = float(input("Ingresa un número: "))
diferencia  = 17 - numero
doble_diferencia = (numero - 17) * 2

if numero < 17:
    print("La diferencia entre los numeros dados es: ", diferencia )

elif numero == 17:
    print("No hay diferencia")

else:
    print("El doble de la diferencia entre los numeros dados es: ", doble_diferencia )
    
    
# 3. Escribe un script que calcule la suma de 3 números dados por el usuario.
#     Si los valores son iguales deberá imprimir la suma multiplicada por 3
    
numero_1 = float(input("Ingresa el primer número: "))
numero_2 = float(input("Ingresa el segundo número: "))
numero_3 = float(input("Ingresa el tercer número: "))

suma = numero_1 + numero_2 + numero_3

if numero_1 == numero_2 and numero_2 == numero_3:
    print(suma * 3)
else:
    print(suma)      

# 4. Escribe un script que calcule cuantas veces se repite un nombre en una lista de nombres determinada por el usuario.

lista_nombres_2= []
nombre = input("Escribe un nombre: ")
lista_nombres_2.append(nombre)
continuar = input("Deseas continuar?: Y / N ").lower()

while continuar == "y":
      nombre = input("Escribe otro nombre: ")
      lista_nombres_2.append(nombre)
      continuar = input("Deseas continuar?: Y / N ").lower()

      
      while continuar != "y" and continuar != "n":
            print("esa no es una opción valida. Escribe Y para continuar, N para parar.: ")
            continuar = input("Deseas continuar?: Y / N ").lower()


for nombre in lista_nombres_2:
    if lista_nombres_2.count(nombre) > 1:
        print("El nombre: ", nombre, "se repite", lista_nombres_2.count(nombre), "veces")



# 5. Escribe un script que determine si una letra es vocal o no

vocales = ["a", "e", "i", "o", "u"]

caracter = input("Introduce un caracter para saber si es vocal o no: ")

if caracter in vocales:
    print("El caracter ingresado", caracter, "es una vocal")
else:
    print("El caracter ingresado", caracter, "no es una vocal")   

# 6. Escribe un script que detemine si un nombre dado por el usuario se encuentra en una lista de nombres. 
#     La lista puede ser predeterminada o determinada por el usuario

nombres_lista = ["Jorge", "Alfredo", "Irvin", "Mauricio", "Francisco", "Luis", "Miren"]

nombre = input("Introduce un nombre: ").title()

if nombre in nombres_lista:
    print("El nombre 'SI' esta dentro de la lista")
else:
    print("El nombre 'NO' esta dentro de la lista")


# 7. Escribe un script que le pida al usuario un número mínimo y un número máximo de un rango de números.
#     El script debe imprimir cuales de ellos son divisibles entre 3

numero_minimo = int(input("Ingresa el numero minimo: ")) 
numero_maximo = int(input("Ingresa el numero máximo: ")) 

print("Los siguientes numeros son multiplos de 3:")
for i in range(numero_minimo, numero_maximo):
    if i % 3 == 0:
        multiplo_de_3 = i
        print("Número: ", i)

# 8. Escribe un script que convierta una cantidad de segundos dada por el usuario a horas, minutos y segundos.

segundos = int(input("Ingresa los segundos: "))

minutos = segundos // 60
hora = segundos // 3600
minutos_sobrantes = (segundos % 3600) // 60
segundos_sobrantes = segundos % 60


if segundos < 60:
  print("El tiempo que ingresaste equivale a", segundos, "segundos")

elif segundos >= 60 and segundos < 3600:
  print("Los segundos que ingresaste equivalen a :", minutos, "minutos y", segundos_sobrantes, "segundos")

elif segundos >= 3600:
  print("El tiempo que ingresaste equivale a:", hora, "hora(s)", minutos_sobrantes, "minutos y ", segundos_sobrantes, "segundos" )

# 9 Escribe un script que imprima si un string dado por el usuario contiene números o no.

lista_numeros = []
for i in range(1, 100000):
  lista_numeros.append(str(i))

string= input("Ingresa un string")  

for char in string:
   if char in lista_numeros:
      numero_en_string = True 

if numero_en_string == True:
   print("Si hay numeros en el string")