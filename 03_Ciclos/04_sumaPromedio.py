'''Escribe un programa para leer 10 números del teclado y encontrar su suma y promedio.'''

cantidad = 10
num = 0
suma = 0
promedio = 0
for i in range(cantidad):
    num = float(input('Digite un número: '))
    suma += num
promedio = suma/cantidad
print(promedio)
