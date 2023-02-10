'''Escriba un programa para calcular el factorial de un número dado.'''

factorial = 1
num = 9 #int(input('Digite un número entero: '))
while num:
    factorial = factorial * num
    num -= 1
print(factorial)
