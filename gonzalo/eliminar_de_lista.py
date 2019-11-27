def eliminar_elenentos_lista(lista_origen, *n):

    for number in n:
        lista_origen.remove(number)

    return lista_origen


# ----
mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

lista_reducida = eliminar_elenentos_lista(mi_lista, 2, 6, 7, 9)

print(lista_reducida)

