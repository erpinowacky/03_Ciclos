'''Escriba un programa para mostrar el patrón como triángulo con un asterisco. El patrón como
*
**
***
****
*****
****
***
**
*
'''
veces = 2
ast = '*'
while True:
    print(ast)
    ast = '*'
    ast = ast * veces
    veces += 1
    if ast == '*****':
        while True:
            veces -= 1
            ast = '*'
            ast = ast * veces
            print(ast)
            if ast == '*':
                break
        break
