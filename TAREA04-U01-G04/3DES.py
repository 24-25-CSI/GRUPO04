import time
from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
import os

def pad(texto):
    while len(texto) % 8 != 0:
        texto += b' '
    return texto

def generar_clave():
    while True:
        clave = get_random_bytes(24)
        if DES3.adjust_key_parity(clave):
            return clave

def encriptar_archivo(archivo_entrada, archivo_salida, clave):
    cifrador = DES3.new(clave, DES3.MODE_ECB)
    with open(archivo_entrada, 'rb') as f:
        texto_plano = f.read()
    texto_relleno = pad(texto_plano)
    texto_cifrado = cifrador.encrypt(texto_relleno)
    with open(archivo_salida, 'wb') as f:
        f.write(texto_cifrado)

def desencriptar_archivo(archivo_entrada, archivo_salida, clave):
    cifrador = DES3.new(clave, DES3.MODE_ECB)
    with open(archivo_entrada, 'rb') as f:
        texto_cifrado = f.read()
    texto_desencriptado = cifrador.decrypt(texto_cifrado).rstrip(b' ')
    with open(archivo_salida, 'wb') as f:
        f.write(texto_desencriptado)
def contar_caracteres(archivo):
        with open(archivo, 'rb') as f:
            contenido = f.read()
        return len(contenido)
def main():
    tiempo_inicio = time.time()
    
    archivo_entrada = r'10000000p.txt'
    tiempo_lectura_archivo = time.time() - tiempo_inicio
    
    clave = generar_clave()
    tiempo_generacion_clave = time.time() - tiempo_inicio

    archivo_encriptado = os.path.join('C:', 'Users', 'Joel', 'Desktop', 'trabajos', 'Cripto', "archivos", 'encrypted_' + str(int(time.time())) + '.txt')
    archivo_encriptado = r'C:\\Users\\Joel\\Desktop\\trabajos\\Cripto\\archivos\\encrypted_' + str(int(time.time())) + '.txt'
    encriptar_archivo(archivo_entrada, archivo_encriptado, clave)
    tiempo_encriptacion = time.time() - tiempo_inicio

    archivo_desencriptado = os.path.join('C:', 'Users', 'Joel', 'Desktop', 'trabajos', 'Cripto', "archivos", 'decrypted_' + str(int(time.time())) + '.txt')
    archivo_desencriptado = r'C:\\Users\\Joel\\Desktop\\trabajos\\Cripto\\archivos\\decrypted_' + str(int(time.time())) + '.txt'
    desencriptar_archivo(archivo_encriptado, archivo_desencriptado, clave)
    tiempo_desencriptacion = time.time() - tiempo_inicio

    print(f"Tiempo de lectura de archivo: {tiempo_lectura_archivo * 1000:.5f} milisegundos")
    print(f"Tiempo de generación de clave: {tiempo_generacion_clave * 1000:.5f} milisegundos")
    print(f"Tiempo de encriptación: {tiempo_encriptacion * 1000:.5f} milisegundos")
    print(f"Tiempo de desencriptación: {tiempo_desencriptacion * 1000:.5f} milisegundos")
     # Contar caracteres
    caracteres_original = contar_caracteres(archivo_entrada)
    caracteres_encriptado = contar_caracteres(archivo_encriptado)

    print(f"Cantidad de caracteres en el archivo original: {caracteres_original}")
    print(f"Cantidad de caracteres en el archivo encriptado: {caracteres_encriptado}")

if __name__ == "__main__":
    main()
   