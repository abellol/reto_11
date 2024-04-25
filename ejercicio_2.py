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
se define la matriz producto_matrices, allí se evalúa que las columnas de la primera matriz, sean iguales a las filas de la segunda matriz
luego multiplica cada elemento de las columnas de la primera, por las filas de la segunda. Retorna una nueva matriz con las filas de la primera, y las columnas de la segunda. 
"""
def producto_matrices(matriz_1:list, matriz_2:list) -> list: # la función toma como argumento las dos matrices a multiplicar y retorna una nueva matriz
  # si no cumple con las condiciones, retorna un error y su respectivo mensaje
	if len(matriz_1[0]) != len(matriz_2):
		raise ValueError("Las columnas y filas no coinciden con los requisitos solicitados, intente de nuevo...")
  # si cumple las condiciones, se declara la variable que acumulará la suma de cada termino y las dos listas para almacenar las filas y la matriz definitiva
	termino = 0
	fils = []
	mat_def = []
  # se recorre cada posición de las matrices ingresadas, se multiplican filas por columnas y se van agregando a la nueva matriz 
	for i in range (len(matriz_1)): 
		for j in range (len(matriz_2[0])): 
			for h in range (len(matriz_2)):
				termino += (matriz_1[i][h]) * (matriz_2[h][j]) # se multplica cada termino de las filas de la primera, por las columnas de la segunda
			fils.append(termino)
			termino = 0
		mat_def.append(fils) 
		fils = []
	return mat_def # retorna la matriz ya multiplicada con las medidas ya explicadas
if __name__ == "__main__":
  try: 
    # el usuario ingresa el numero de filas y columnas que desea que tengan cada una de sus matrices
    print("su matriz 1 debe tener el mismo numero de columnas que filas la matriz 2")
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

    matriz_1 = generar_matriz(filas_1, columnas_1) # genera e imprime la primera matriz
    print("matriz 1:")
    imprimir_matriz(matriz_1)

    matriz_2 = generar_matriz(filas_2, columnas_2) # genera e imprime la segunda matriz
    print("matriz 2:")
    imprimir_matriz(matriz_2)

    print(f"matriz 1 * matriz 2= ")
    imprimir_matriz(producto_matrices(matriz_1, matriz_2)) # imprime la matriz resultante del producto de las dos anteriores
  except ValueError as error: # en caso de cualquier caracter que no se un numero entero, retorna un error y su respectivo mensaje
    print(f"{error} \n") 