
def calcular(primer_numero, operacion, segundo_numero):

    if operacion == '+':
        resultado = primer_numero + segundo_numero
        print(f'resultado: {resultado}')
    elif operacion == '-':
        resultado = primer_numero - segundo_numero
        print(f'resultado: {resultado}')
    elif operacion == 'x':
        resultado = primer_numero * segundo_numero
        print(f'resultado: {resultado}')
    elif operacion == '/':
        resultado = primer_numero / segundo_numero
        print(f'resultado: {resultado}')

    primer_numero = resultado
    operacion = input(" operación? < +  ,  -  ,   x  ,  / > : ")
    segundo_numero = int(input(" -> siguiente número: "))

    calcular(primer_numero, operacion, segundo_numero)


# --------

primer_numero = int(input(" -> primer número: "))
operacion = input(" operación? < +  ,  -  ,   x  ,  / > : ")
segundo_numero = int(input(" -> segundo número: "))

calcular(primer_numero, operacion, segundo_numero)

