# Reto 11: Matrices
### Soy Alejandro Bello y pertenezco al grupo de "Fenomenoides", adjunto nuestro logo: 

<details><summary>Preparense para ver el grandioso logo: </summary><p>
<div align='center'>
<figure> <img src="https://i.postimg.cc/NFbwf57S/logo-def.png" alt="Defensa Civil" width="400" height="auto"/></br>
<figcaption><b> "somos programadores, no diseñadores" </b></figcaption></figure>
</div>
</p></details><br>
a continuación se encuentra el desarrollo de los 5 ejercicios planteados referente al uso de matrices, en ellos se evidencia el uso de funciones y métodos para manipular datos de listas y matrices (listas de listas).

## Funciones generales del reto
Dentro del reto se implementaron dos funciones esenciales, una para mostrar las matrices generadas y que se distingan sus m y n dimensiones, y la otra para que a partir de datos esenciales como el numero de columnas y filas, permita ingresar los datos de la matriz; retornando como resutado la matriz ingresada por la consola.
```python
"""
se define la función imprimir matriz, para que muestre de una manera mas clara la forma de la matriz
y se distingan sus n y m dimensiones.
"""
def imprimir_matriz(mat):
  for i in mat:
    print (i)
  print("---------------------------------")

"""
La funcion mediante bucles y listas vacías almacena y ordena los valores ingresados por la consola en la
cantidad de filas y columnas previamente ingresados como argumentos de la función
"""
def generar_matriz(filas : int, columnas : int) -> list: # la función toma como argumento el numero de filas y columnas, retorna la matriz
  # se declaran dos listas vacías las cuales almacenarán las filas (fils) y la matriz final (matriz)
  fil : list = []
  matriz : list = []
  # se declara una variable iteradora que solamente muestra el numero de dato y la posición donde irá
  num_dato : int = 1
  # los bucles for recorren cada posición de la matriz que se genera
  for i in range (filas):
    for j in range (columnas):
      # la lista vacía fils, almacena cada fila de datos que son ingresador por el usuario
      fil.append(int(input(f"ingrese el dato {num_dato} que va en la posición {i + 1, j + 1} de la matriz:  ")))
      num_dato += 1
    # la matriz final almacena los valores que guardó fils y luego fils se vacía para almacenar la nueva fila de datos
    matriz.append(fil)
    fil = []
  print("")
  return matriz
```
## 1. Desarrolle un programa que permita realizar la suma/resta de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.
Para el desarrollo del programa se utilizaron ciclos `while` para verificar que los datos ingresados por el usuario sean correctos y cumplan las condiciones para poder realizar la operación (la función también verifica que ambas matrices sean de igual tamaño), también dentro de la funcion `suma_matrices` se utlizan los bucles `for` para recorrer las filas (variable iteradora "i") y las columnas (variable iteradora "j") de la matriz, permitiendo sumar las valores de cada posición.
```python
def imprimir_matriz(mat):
  for i in mat:
    print (i)
  print("-------------------------")  
def generar_matriz(filas : int, columnas : int) -> list:
  fil : list = []
  matriz : list = []
  num_dato : int = 1
  fila = filas
  columna = columnas
  for i in range (fila):
    for j in range (columna):
      fil.append(int(input(f"ingrese el dato {num_dato} de la primera matriz:  ")))
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

  except ValueError as error: # en caso de cualquier caracter que no sea un numero entero, retorna un error y su respectivo mensaje
    print(f"{error}, intente de nuevo... \n")
```
## 2. Desarrolle un programa que permita realizar el producto de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.
Al igual que en el ejercicio anterior se verifica con los ciclos `while` que los datos ingresados son positivos (necesarios para crear una matriz), por otro lado, dentro la función `producto_matrices`se verifica que las columnas de la matriz 1 son iguales a las filas de la matriz 2 y calcula el producto multiplicando los elementos de cada fila por cada columna, retornando una matriz nueva con las filas de la matriz 1 y las columnas de la matriz 2.
```python
def imprimir_matriz(mat):
  for i in mat:
    print (i)
  print("-------------------------")  
def generar_matriz(filas : int, columnas : int) -> list:
  fil : list = []
  matriz : list = []
  num_dato : int = 1
  fila = filas
  columna = columnas
  for i in range (fila):
    for j in range (columna):
      fil.append(int(input(f"ingrese el dato {num_dato} de la primera matriz:  ")))
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
```
## 3. Desarrolle un programa que permita obtener la matriz transpuesta de una matriz ingresada. El programa debe validar las condiciones necesarias para ejecutar la operación.
Mediante un bucle `while` se verifica que no hayan valores con los que no se puede generar matrices, por otro la funcion `transpuesta` intercambia de posición los valores de las filas, con las columnas y retorna esa nueva matriz que simplemente "cambió de orientación", mas no cambiaron sus datos
```python
def imprimir_matriz(mat):
  for i in mat:
    print (i)
  print("-------------------------")  
def generar_matriz(filas : int, columnas : int) -> list:
  fil = []
  matriz = []
  num_dato : int = 1
  fila = filas
  columna = columnas
  for i in range (fila):
    for j in range (columna):
      fil.append(int(input(f"ingrese el dato {num_dato} de la primera matriz")))
      num_dato += 1
    matriz.append(fil)
    fil = []
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
```
## 4. Desarrollar un programa que sume los elementos de una columna dada de una matriz.
Se utliza el mismo algoritmo de bucles `for` anidados para acceder a los elementos de la lista, en esta función `suma_columna` se obtienen todos los valores de la columna dada por el usuario y posteriormente, se retorna la suma de estos elementos
```python
def imprimir_matriz(mat):
  for i in mat:
    print (i)
  print("-------------------------")  
def generar_matriz(filas : int, columnas : int) -> list:
  fil = []
  matriz = []
  num_dato : int = 1
  fila = filas
  columna = columnas
  for i in range (fila):
    for j in range (columna):
      fil.append(int(input(f"ingrese el dato {num_dato} de la primera matriz")))
      num_dato += 1
    matriz.append(fil)
    fil = []
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
```
## 5. Desarrollar un programa que sume los elementos de una fila dada de una matriz.
al igual que el anterior, utliza el mismo algoritmo, sin embargo, en este caso accede es a todos los datos de una fila ingresada por el usuario y retorna la suma de estos, sin modificar los datos de la matriz original.
```python
def imprimir_matriz(mat):
  for i in mat:
    print (i)
  print("-------------------------")  
def generar_matriz(filas : int, columnas : int) -> list:
  fil = []
  matriz = []
  num_dato : int = 1
  fila = filas
  columna = columnas
  for i in range (fila):
    for j in range (columna):
      fil.append(int(input(f"ingrese el dato {num_dato} de la primera matriz")))
      num_dato += 1
    matriz.append(fil)
    fil = []
  return matriz
"""
se define la función "suma_fila" donde se accede a la fila ingresada por el usuario y suma todos los elementos de esta
"""
def suma_fila(matriz : list, n_fila : int) -> float: # la funcion toma como argumento la matriz ingresada y la fila deseada por el usuario y retorna el valor de la suma
  #  se declara una lista vacía, donde se guardarán todos los valores de la fila y una variable suma donde se guardará la suma de todos los elementos de la fila
  suma_ac : float = 0
  lista_suma = []
  for i in range (n_fila, n_fila + 1):
    for j in range (len(matriz[0])):
      # se accede a cada elemento de la fila y se suma con el anterior
      suma_ac += (matriz[i][j])
      lista_suma.append(matriz[i][j])
  return (f"{lista_suma} = {suma_ac}") #  se retorna un string con la lista de elementos de la columna y la suma de estos

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
    n_fila = int(input(f"Ingrese la fila que desea sumar (debe estar entre 1 y {filas_1})"))
    # mediante un bucle se verifica que esté dentro del rango de valores (cantidad de columnas) 
    while n_fila < 1 or n_fila > columnas_1:
      n_fila = int(input(f"no está dentro del rango esperado, ingrese la columna que desea sumar (debe estar entre 1 y {columnas_1})"))
    print(suma_fila(matriz_1, n_fila - 1)) # imprime la suma de n columna
  except ValueError: # en caso de cualquier caracter que no se un numero entero, retorna un error y su respectivo mensaje
    print("El caracter ingresado no es un numero... ")
```
