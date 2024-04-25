def imprimir_matriz(mat):
  for i in mat:
    print (i)
  print("---------------------------------")
def generar_matriz(filas : int, columnas : int) -> list:
  fil : list = []
  matriz : list = []
  num_dato : int = 1
  for i in range (filas):
    for j in range (columnas):
      fil.append(int(input(f"ingrese el dato {num_dato} que va en la posición {i + 1, j + 1} de la matriz:  ")))
      num_dato += 1
    matriz.append(fil)
    fil = []
  print("")
  return matriz
"""
Se define la función "suma_matrices" donde se evalúa que ambas matrices tengan el mismo numero tanto de filas
como de columnas, luego suma los elementos que están en la misma posición de cada matriz y genera una nueva matriz
que tiene las mismas medidas que las originales 
"""
def suma_matrices(matriz_1:list, matriz_2:list) -> list: # la funcion toma como argumentos las dos matrices que se van a sumar y retorna una nueva matriz
  # la funcion verifica que las matrices tengan el mismo numero de columnas y filas
  if len(matriz_1) != len(matriz_2) or len(matriz_1[0]) != len(matriz_2[0]):
    raise ValueError ("las matrices tienen diferentes tamaños") # en caso de que no, retorna un error 
  # si cumple las condiciones, se declaran dos listas vacías para acumular las nuevas filas y la matriz nueva
  fils = []
  mat_def = []
  # se usa el mismo algoritmo que se usó para generar listas pero almacena la suma de las i, j elementos de cada matriz
  for i in range(len(matriz_1)): 
    for j in range(len(matriz_1[0])):
      termino = (matriz_1[i][j]) + (matriz_2[i][j]) # se calcula la suma y se agrega a la misma posición en la matriz
      fils.append(termino)
    mat_def.append(fils)
    fils = [] 
  return mat_def # retorna la matriz definitiva calculada


if __name__ == "__main__":
  try:
    # el usuario ingresa el numero de filas y columnas que desea que tengan cada una de sus matrices
    print("sus matrices deben tener el mismo tamaño")
    filas_1 = int(input("Ingrese el numero de filas de su primera matriz: "))
    columnas_1 = int(input("Ingrese el numero de columnas de su primera matriz: "))
    filas_2 = int(input("Ingrese el numero de filas de su segunda matriz: "))
    columnas_2 = int(input("Ingrese el numero de columnas de su segunda matriz: "))
    # se comprueba que no hayan cantidades negativas ni nulas para generar la matriz
    while (filas_1 and filas_2) <= 0 or (columnas_1 and columnas_2) <= 0:
      filas_1 = int(input("no hay cantidades negativas ni inexistentes, ingrese el numero de filas de su primera matriz: "))
      columnas_1 = int(input("no hay cantidades negativas ni inexistentes, ingrese el numero de columnas de su primera matriz: "))
      filas_2 = int(input("no hay cantidades negativas ni inexistentes, ingrese el numero de filas de su segunda matriz: "))
      columnas_2 = int(input("no hay cantidades negativas ni inexistentes, ingrese el numero de columnas de su segunda matriz: "))
    print("----------------------------------------")

    # se generan las matrices y se calcula la suma de estas 
    matriz_1 = generar_matriz(filas_1, columnas_1) # genera la matriz 1 
    print("matriz 1 \n")
    imprimir_matriz(matriz_1)  

    matriz_2 = generar_matriz(filas_2, columnas_2) # genera la matriz 2
    print("matriz 2 \n")
    imprimir_matriz(matriz_2)

    print("matriz 1 + matriz 2 = \n") 
    imprimir_matriz(suma_matrices(matriz_1, matriz_2)) # se genera e imprimime la matriz resultante de la suma de las dos anteriores
  except ValueError as error: # en caso de cualquier caracter que no se un numero entero, retorna un error y su respectivo mensaje
    print(f"{error}, intente de nuevo... \n")
