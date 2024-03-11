# Ejercicio 1
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    print(numero)


# Ejercicio 2
def suma(a, b, c):
    return a + b + c

resultado = suma(4, 1, 7)
print(resultado)


# Ejercicio 3
suma_lambda = lambda a, b, c: a + b + c

resultado = suma_lambda(8, 3, 6)
print(resultado)  


# Ejercicio 4
nombre = 'Enrique'

lista_nombre = ('Jessica', 'Paul', 'George', 'Henry', 'Adán')

coincidencia = False

for nombre_lista in lista_nombre:
    if nombre == nombre_lista:
        coincidencia = True
        break

if coincidencia:
    print(f"El nombre {nombre} coincide.")
else:
    print(f"El nombre {nombre} no coincide.")
