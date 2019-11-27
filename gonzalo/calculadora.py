
def calcular(primer_numero, segundo_numero):
    operacion = input(" operación? < +  ,  -  ,   x  ,  / > : ")

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
    segundo_numero = int(input(" -> siguiente número: "))

    calcular(primer_numero, segundo_numero)


# --------

primer_numero = int(input(" -> primer número: "))
segundo_numero = int(input(" -> segundo número: "))

calcular(primer_numero, segundo_numero)

