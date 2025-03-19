def ordenar_fila(matriz, fila_indice):
    """Ordena una fila específica de una matriz."""
    fila = matriz[fila_indice]
    fila.sort()  # Ordena la fila en orden ascendente
    return matriz

# Matriz de ejemplo
matriz = [[9, 2, 7], [4, 5, 6], [1, 8, 3]]
fila_a_ordenar = 0

print("Matriz original:", matriz)
matriz_ordenada = ordenar_fila(matriz, fila_a_ordenar)
print(f"Matriz con fila {fila_a_ordenar} ordenada:", matriz_ordenada)