'''Escriba un programa para mostrar la tabla de multiplicar de un entero dado.'''

num1 = int(input('Digite el número de la tabla: '))
num2 = int(input('Digite primer número: '))
num3 = int(input('Digite el segundo número: '))

while num2 <= num3:
    multi = num1 * num2
    print(f'{num1} * {num2} = {multi}')
    num2 += 1
    