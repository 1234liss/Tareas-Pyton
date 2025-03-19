def buscar_valor(matriz, valor):
    """Busca un valor en una matriz bidimensional."""
    for i, fila in enumerate(matriz):
        for j, elemento in enumerate(fila):
            if elemento == valor:
                return True, i, j  # Valor encontrado, devuelve True y la posición
    return False, None, None  # Valor no encontrado

# Matriz de ejemplo
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

valor_buscado = 5
encontrado, fila, columna = buscar_valor(matriz, valor_buscado)

if encontrado:
    print(f"Valor {valor_buscado} encontrado en la posición ({fila}, {columna})")
else:
    print(f"Valor {valor_buscado} no encontrado en la matriz")