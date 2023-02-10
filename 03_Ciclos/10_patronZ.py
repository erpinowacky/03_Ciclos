'''Escriba un programa para mostrar un patrón como Z con asteriscos. 
 0123456       
0*******       
1     *        
2    *         
3   *          
4  *
5 *
6*******
'''
contador1 = 5
contador2 = 0
ast = '*'
while contador1 :    
    while contador1:
        print(ast, end='')
        contador2 += 1
        if contador2 == contador1:
            ast = '*'
            print(ast)
            ast = ' ' 
            contador2 = 0
            contador1 -= 1
            break
    if contador1 == contador2:
        contador2 = 6
        ast = '*'
        while contador2:
            print(ast, end='')
            contador2 -=1
        break