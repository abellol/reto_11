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
Se defina la función de "suma_columna" donde accede a la columna ingresada por el usuario y suma todos los elementos en esta
"""
def suma_columna(matriz : list, n_columna : int) -> float: # la funcion toma como argumento una matriz y el numero de columna, retorna el valor de la suma
  # se declara una lista vacía, donde se guardarán todos los valores de la columna y una variable suma donde se guardará la suma de todos los elementos de la columna
  suma_ac : float = 0
  lista_suma = []
  for i in range (n_columna, n_columna + 1):
    for j in range (len(matriz)):
      # se accede a cada elemento de la columna y se suma con el anterior
      suma_ac += (matriz[j][i]) 
      lista_suma.append(matriz[j][i])
  return (f"{lista_suma} = {suma_ac}") # se retorna un string con la lista de elementos de la columna y la suma de estos

if __name__ == "__main__":
  try:
    # el usuario ingresa el numero de filas y columnas que desea que tengan cada una de sus matrices
    filas_1 = int(input("Ingrese el numero de filas de su primera matriz: "))
    columnas_1 = int(input("Ingrese el numero de columnas de su primera matriz: "))
    # se comprueba que no hayan cantidades negativas ni nulas para generar la matriz
    while filas_1 <= 0 or columnas_1 <= 0:
      filas_1 = int(input("no hay cantidades negativas ni inexistentes, ingrese el numero de filas de su primera matriz: "))
      columnas_1 = int(input("no hay cantidades negativas ni inexistentes, ingrese el numero de columnas de su primera matriz: "))
        
    matriz_1 = generar_matriz(filas_1, columnas_1) # se genera e imprime la matriz 1
    print("matriz 1:")
    imprimir_matriz(matriz_1)
    # el usuario ingresa la columna que desea sumar
    n_columna = int(input(f"Ingrese la columna que desea sumar (debe estar entre 1 y {columnas_1})"))
    # mediante un bucle se verifica que esté dentro del rango de valores (cantidad de columnas) 
    while n_columna < 1 or n_columna > columnas_1:
      n_columna = int(input(f"no está dentro del rango esperado, ingrese la columna que desea sumar (debe estar entre 1 y {columnas_1})"))
          
    print(suma_columna(matriz_1, n_columna - 1)) # imprime la suma de n columna
  except ValueError: # en caso de cualquier caracter que no se un numero entero, retorna un error y su respectivo mensaje
    print("el caracter ingresado no es un numero...")