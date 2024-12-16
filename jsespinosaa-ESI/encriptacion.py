def cifrado_permutacion_filas(mensaje, filas=5):
    #matriz=[]
    # Reemplazar espacios con '-'
    mensaje = mensaje.replace(' ', '-')
    
    
    # Calcular el número de columnas necesarias
    # Dividimos la longitud del mensaje + el numero de filas definido entre el número de filas y redondeamos hacia arriba
    columnas = (len(mensaje) + filas - 1) // filas
    if columnas < 3:
        columnas = 3
    
    # Crear la matriz de cifrado
    # Se crea una matriz (FxC) de tamaño 'filas' x 'columnas'
    # Cada elemento de la matriz se inicializa con el carácter '*' matriz llena de '*'
    matriz = [['*' for _ in range(columnas)] for _ in range(filas)]
    
    # Llenar la matriz con el mensaje
    index = 0
    
    for i in range(filas):
        for j in range(columnas):
            if index < len(mensaje):
                #Salto a la siguiente fila
                matriz[i][j] = mensaje[index]
                index += 1

    # Inicializar el mensaje en vacio
    mensaje_cifrado = ''
    
    # Leer el mensaje cifrado columna por columna
    for j in range(columnas):
        for i in range(filas):
            mensaje_cifrado += matriz[i][j]
    # Devuelve el mensaje cifrado y la matriz para imprimir luego
    return mensaje_cifrado, matriz

def imprimir_matriz(matriz):
    print("----------MATRIZ-----------")
    # Impresion de la matriz 
    for fila in matriz:
        print(' '.join(fila))
# Ejemplo de uso
mensaje = input("Introduce el mensaje a cifrar: ")
#mensaje = "este es un mensaje de prueba"
mensaje_cifrado = cifrado_permutacion_filas(mensaje)
mensaje_cifrado, matriz = cifrado_permutacion_filas(mensaje)
imprimir_matriz(matriz)
print("-----------MENSAJE CIFRADO")
print(mensaje_cifrado)