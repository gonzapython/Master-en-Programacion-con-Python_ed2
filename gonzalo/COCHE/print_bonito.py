
def imprimir_bonito(diccionario):
    key = diccionario.keys()        # lista de claves
    values = diccionario.values()   # lista de valores

    for clave in key:
        print(f'|---{clave}---|')





# ---
usu = {'nombre': 'Alberto', 'aficion': 'scrapping', 'edad':'26'}

imprimir_bonito(usu)