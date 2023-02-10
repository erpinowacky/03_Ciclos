'''Escriba un programa para mostrar n términos de número natural y su suma (Fibonacci).'''

fibonacci = 10 #int(input('Digite un número entero: '))
num1 = 1
num2 = 0
resultado = 0

for i in range(fibonacci+1):
    resultado = num1 + num2
    num2 = num1
    num1 = resultado 
    print(resultado)        
