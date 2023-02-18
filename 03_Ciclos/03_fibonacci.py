'''Escriba un programa para mostrar n términos de número natural y su suma (Fibonacci).'''

fibonacci = 5 #int(input('Digite un número entero: '))
num1 = 0
num2 = 0
resultado = 0

for i in range(fibonacci):
    if i == 0:
        pass
    elif i == 1:
        resultado = 1
        num1 = resultado
    else:
        resultado = num1 + num2
        num2 = num1
        num1 = resultado 
    print(resultado)       
