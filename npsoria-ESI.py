""" Realice el cifrado de un mensaje por permutación de filas, teniendo como clave 5 filas y
 la cantidad de columnas que sean necesarias (garantice al menos 3) 
 los espacios del mensaje original se sustituyen con el carácter "-", 
 si en la matriz de cifrados obran espacio estos deben llenarse con el carácter “*” """

import math

def cifrar_por_permutacion(mensaje, num_filas=5):

    # Reemplazamos los espacio con -
    mensaje = mensaje.replace(' ', '-')
    
    #numero de columnas
    num_columnas = math.ceil(len(mensaje) / num_filas)
    
    #Rellenamos con * si es necesario
    mensaje = mensaje.ljust(num_filas * num_columnas, '*')

    #Creamos la matriz de cifrado
    matriz_mensaje = [list(mensaje[i:i + num_columnas]) for i in range(0, len(mensaje), num_columnas)]
    print(matriz_mensaje)

    #leemos por columnas el mensaje cifrado
    mensaje_cifrado = ''.join(''.join(fila[i] for fila in matriz_mensaje) for i in range(num_columnas))
    
    return mensaje_cifrado

mensaje_original = "hola mundo mensaje de prueba"
mensaje_cifrado = cifrar_por_permutacion(mensaje_original, 5)
print("mensaje original:", mensaje_original)
print("mensaje cifrado:", mensaje_cifrado)
