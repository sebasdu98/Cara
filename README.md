# Caracol

## Integrante:
  * Sebastian Duque Gallego    20162020039
 
#### Introduccion:
El proposito de este proyecto es recibir un archivo txt el cual contenga una matriz cuadrada, consiste en imprimirla como si fuera en caracol,Como en la imagen que se observa,obviamente sin repetir ninguna fila o columna que ya se imprimiera ![asd](https://user-images.githubusercontent.com/42306260/52100943-a59ff300-25a7-11e9-8463-d0565cae2c65.jpg)

#### Funciones:
 * cargar_archivo: Funcion que retorna el archivo de texto
 * crear_mat: Funcion que recibe un archivo de texto y lo ingresa en una matriz vacia y posteriormente retornar la matriz llena con el archivo de texto
 * moverDer: Funcion que recibe una matriz,fila,columna, un auxiliar y por el ultimo de primeras el tamaño de la matriz,segun la columna que recibe empezara a recorrerla hasta donde pueda y llamara a la funcion moverAba mientras tamaño sea mayor a 0 y restara uno al tamaño.Si el tamaño es 0 significa que terminara el programa
 * moverAba:Funcion que recibe una matriz,fila,columna, un auxiliar y por el ultimo un tamaño,quedara en la columna que se quedo moverDer y empezara a bajar hasta donde pueda y llamara a la funcion moverIzq mientras el tamaño sea mayor a 0.Si el tamaño es 0 significa que terminara el programa
 * moverIzq:Funcion que recibe una matriz,fila,columna, un auxiliar y por el ultimo un tamaño,quedara en la fila que se quedo moverAba y empezara a devolverse por las columnas hasta donde pueda y llamara a la funcion moverArr mientras el tamaño sea mayor a 0 y restara uno al tamaño.Si el tamaño es 0 signifca que terminara el programa
 * moverArr:Funcion que recibe una matriz,fila,columna, un auxiliar y por el ultimo un tamaño,quedara en la columna que se quedo moverIzq y empezara a devolverse por las filas hasta donde pueda y llamara a la funcion moverDer mientras el tamaño sea mayor a 0.Si el tamaño es 0 signifca que terminara el programa
 * resolver: Esta funcion es la que inicia el programa y llamara a la funcion moverDer desde la columna 0 y fila 0
