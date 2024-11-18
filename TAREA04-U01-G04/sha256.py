import hashlib
import time
import chardet  # Para detectar la codificación

# Función para generar el hash SHA-256 de un archivo
def generar_hash_sha256(ruta_archivo):
    # Detectar la codificación del archivo
    with open(ruta_archivo, 'rb') as archivo:
        datos_crudos = archivo.read()
        resultado = chardet.detect(datos_crudos)
        codificacion = resultado['encoding']
    
    # Medir el tiempo de la lectura del archivo
    inicio_lectura = time.time()
    
    with open(ruta_archivo, 'r', encoding=codificacion) as archivo:
        contenido = archivo.read()
    
    # Tiempo de lectura en milisegundos
    tiempo_lectura = (time.time() - inicio_lectura) * 1000  # Convertir a milisegundos
    
    # Medir el tiempo para generar el hash SHA-256
    inicio_hash = time.time()
    objeto_hash = hashlib.sha256(contenido.encode())
    hash_hexadecimal = objeto_hash.hexdigest()
    tiempo_hash = (time.time() - inicio_hash) * 1000  # Convertir a milisegundos
    
    # Tiempo total en milisegundos
    tiempo_total = tiempo_lectura + tiempo_hash
    
    # Imprimir resultados
    print(f"\nHash SHA-256 del archivo {ruta_archivo}:")
    print(f"{hash_hexadecimal}")
    print(f"Tiempo de lectura: {tiempo_lectura:.6f} ms")
    print(f"Tiempo de encriptado (hash): {tiempo_hash:.6f} ms")
    print(f"Tiempo total (lectura + encriptado): {tiempo_total:.6f} ms")
    
    return tiempo_lectura, tiempo_hash, tiempo_total, hash_hexadecimal  # Devolvemos el hash también

# Función principal que ejecuta el proceso para los archivos
def ejecutar_sha256_para_archivos():
    # Archivos a procesar (asegúrate de que estén en la misma carpeta que el script)
    rutas_archivos = ["10p.txt", "100p.txt", "1000p.txt", "10000p.txt", "100000p.txt", "1000000p.txt", "10000000p.txt"]
    
    resultados = []
    
    for ruta_archivo in rutas_archivos:
        tiempo_lectura, tiempo_hash, tiempo_total, valor_hash = generar_hash_sha256(ruta_archivo)
        
        # Guardar los resultados
        resultados.append({
            "archivo": ruta_archivo,
            "hash": valor_hash,
            "tiempo_lectura": tiempo_lectura,
            "tiempo_hash": tiempo_hash,
            "tiempo_total": tiempo_total,
            "num_palabras": len(open(ruta_archivo, 'r').read().split()),  # Número de palabras
            "num_caracteres_entrada": len(open(ruta_archivo, 'r').read()),  # Número de caracteres de entrada
            "num_caracteres_salida": 64  # SHA-256 siempre tiene 64 caracteres de salida
        })
    
    # Mostrar la tabla resumen
    print("\nResumen de resultados:")
    print("Archivo      | Hash                                      | Num Palabras | Caract Entrada | Caract Salida | T-E1 (Lectura) | T-E2 (Hash) | T-Total")
    for resultado in resultados:
        print(f"{resultado['archivo']:<12} | {resultado['hash']:<40} | {resultado['num_palabras']:<13} | {resultado['num_caracteres_entrada']:<14} | {resultado['num_caracteres_salida']:<13} | {resultado['tiempo_lectura']:.6f} | {resultado['tiempo_hash']:.6f} | {resultado['tiempo_total']:.6f}")

# Llamar a la función principal
ejecutar_sha256_para_archivos()
