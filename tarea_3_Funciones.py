# 1. Escribe una función qué reciba varios números y devuelva el mayor de ellos.
def largest_number():
    numbers_list = []
    while True:
        number = int(input("Please enter a number: "))
        numbers_list.append(number)
        add_number = input("Do you want to add more numbers: Y / N").lower()

        while add_number != "y" and add_number != "n":
            print("This is not a valid answer. Type Y or N: ")
            add_number = input("Do you want to add more numbers: Y / N").lower()

        if add_number == "n":
            break

    max_number = numbers_list[0]

    for i in numbers_list:
        if i > max_number:
            max_number = i
    print()
    print("The largest number is: ")
    return max_number


largest_number()

# 2. Escribe una función que permita multiplicar varios números


def product(*args):
    start = 1
    for i in args:
        start *= i
    return start


product(5, 3, 7, 9, 6)


# 3.Escribe una función para verificar que un número se encuentra en un rango de números determinado. El resultado de esa función debe ser booleano


def number_in_range():
    print("Enter a range of numbers")
    min_number = int(input("Enter the smallest number: "))
    max_number = int(input("Enter the largest number: "))

    number = int(input("Enter the number that you want to search: "))

    is_in_range = False

    for i in range(min_number, max_number):
        if number >= min_number and number <= max_number:
            is_in_range = True
    print(is_in_range)


number_in_range()


# 4.Escribe una función que permita identificar si un número dado es primo o no.
def is_prime(number):
    is_prime = False
    if number == 1:
        is_prime = False
    elif number == 2 or number == 3 or number == 7:
        is_prime = True
    elif number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number % 7 == 0:
        is_prime = False
    else:
        is_prime = True

    if is_prime == True:
        print("El numero ES primo")
    else:
        print("El numero NO ES primo")


is_prime(43)

# 5.Escribe un programa que pueda identificar si una palabra o frase es un palíndromo (https://es.wikipedia.org/wiki/Pal%C3%ADndromo).


def palindromo(word):
    word = list(word)
    reverse_word = []
    idx = len(word) - 1

    for char in word:
        reverse_word.append(word[idx])
        idx -= 1

    if word == reverse_word:
        print("The word you entered IS PALINDROMO")
    else:
        print("The word you entered IS NOT PALINDROMO")


palindromo("somos")


# 6.Escribe una función que genere una lista con los números de la serie de fibonacci. La función debe recibir la cantidad de números a generar
def fibonacci(a):
    n_1 = 0
    n_2 = 1
    print(n_1)
    print(n_2)

    for i in range(a - 2):
        n_3 = n_1 + n_2
        n_1 = n_2
        n_2 = n_3
        print(n_3)


fibonacci(12)


# 8. Escribe un programa tipo "Caja registradora", que permita introducir una lista de artículos, cantidad y precio. Al final debe mostrarle al usuario la cantidad de artículos y la cantidad a

import random

print("Welcome to the Cash Register Program")
cash_register_dict = {}
is_continue = True

while is_continue == True:
    article_dict = {}
    article_id = str(random.randint(0, 100))
    item = input("Type the name of the article: ")
    quantity = int(input("Enter the quantity: "))
    price = float(input("Enter the price: "))
    cash_register_dict["Article " + article_id] = article_dict
    article_dict["Item"] = item
    article_dict["Quantity"] = quantity
    article_dict["Price"] = price
    add_article = input("Do you want to add another article?: Y / N").lower()

    valid_options = ["y", "n"]
    while add_article not in valid_options:
        print("This is not a valid option. Type 'y' or 'n' ")
        add_article = input("Do you want to add another article?: Y / N").lower()

    if add_article == "n":
        is_continue = False

total_qty = 0
total_amount = 0

print("Checkout")
print()

for key, value in cash_register_dict.items():
    item_amount = cash_register_dict[key]["Quantity"] * cash_register_dict[key]["Price"]
    total_qty += cash_register_dict[key]["Quantity"]
    total_amount += item_amount
    print(
        "Article:",
        cash_register_dict[key]["Item"].title(),
        "| Quantity: ",
        cash_register_dict[key]["Quantity"],
        "| Price:",
        cash_register_dict[key]["Price"],
        "| Item Total: ",
        item_amount,
    )


print()
print("Total Quantity: ", total_qty)
print()
print("Subtotal_amount: ", total_amount)
print()
print("Total Amount:", round(total_amount * 1.16, 2))
