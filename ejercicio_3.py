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
Se defina la función transpuesta, donde intercambia de posición las filas y columnas de una matriz ingresada
"""
def transpuesta(matriz : list) -> list: # la funcion toma como argumento una lista y luego retorna otra lista
  # se declaran las listas que almacenarán las nuevas filas y la nueva matriz definitiva
  mat_nueva : list = []
  fila : list = []
  # se accede a cada elemento de la lista original, y se generan nuevas filas del tamaño de las columnas de la matriz original
  for i in range (len(matriz[0])):
    for j in range (len(matriz)):
      fila.append(matriz[j][i])
    mat_nueva.append(fila)
    fila=[]
  print(f"matriz transpuesta:")
  return mat_nueva # retorna la matriz nueva donde solo se intercambiaron de posición los valores
      
if __name__ == "__main__":
  try:
    # el usuario ingresa el numero de filas y columnas que desea que tengan cada una de sus matrices
    filas_1 = int(input("Ingrese el numero de filas de su primera matriz: "))
    columnas_1 = int(input("Ingrese el numero de columnas de su primera matriz: "))
    # se comprueba que no hayan cantidades negativas ni nulas para generar la matriz
    while filas_1 <= 0 or columnas_1 <= 0:
      filas_1 = int(input("no hay cantidades negativas ni inexistentes, ingrese el numero de filas de su primera matriz: "))
      columnas_1 = int(input("no hay cantidades negativas ni inexistentes, ingrese el numero de columnas de su primera matriz: "))

    matriz_1 = generar_matriz(filas_1, columnas_1) # se genera la matriz 1 
    print("matriz 1:")
    imprimir_matriz(matriz_1)

    imprimir_matriz(transpuesta(matriz_1)) #imprime y retorna la nueva matriz
  except ValueError: # en caso de cualquier caracter que no se un numero entero, retorna un error y su respectivo mensaje
    print("el caracter ingresado no es un numero...")