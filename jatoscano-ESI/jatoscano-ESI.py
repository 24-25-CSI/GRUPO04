def cifrar_mensaje(mensaje):
    
    # Reemplazar espacios con "-"
    mensaje = mensaje.replace(" ", "-")
    
    # Determinar el número de columnas necesarias
    filas = 5
    columnas = max(3, (len(mensaje) + filas - 1) // filas)
    
    # Crear la matriz de cifrado
    matriz = [['*' for _ in range(columnas)] for _ in range(filas)]
    
    # Llenar la matriz con el mensaje
    indice = 0
    for i in range(filas):
        for j in range(columnas):
            if indice < len(mensaje):
                matriz[i][j] = mensaje[indice]
                indice += 1
    
    # Imprimir la matriz
    for fila in matriz:
        print(" ".join(fila))
    
    # Leer la matriz por columnas para obtener el mensaje cifrado
    mensaje_cifrado = ""
    for j in range(columnas):
        for i in range(filas):
            mensaje_cifrado += matriz[i][j]
    
    return mensaje_cifrado

# Elegir la palabra a cifrar
mensaje = "Prueba de Criptografia"
mensaje_cifrado = cifrar_mensaje(mensaje)

# Imprimir el mensaje cifrado
print("Mensaje Cifrado: " + mensaje_cifrado)