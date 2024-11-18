import time
from ecdsa import SigningKey, SECP256k1

def read_file(file_path):
    start_time = time.time()
    with open(file_path, 'r') as file:
        data = file.read()
    end_time = time.time()
    te1 = (end_time - start_time) * 1000
    print(f"T-E1: Tiempo de lectura de archivo: {te1} segundos")
    return data, te1

def generate_keys():
    start_time = time.time()
    private_key = SigningKey.generate(curve=SECP256k1)
    public_key = private_key.get_verifying_key()
    end_time = time.time()
    te2 = (end_time - start_time) * 1000
    print(f"T-E2: Tiempo de generación de claves: {te2} segundos")
    return private_key, public_key, te2

def encrypt_message(message, public_key):
    start_time = time.time()
    encrypted_message = public_key.to_string().hex() + message
    end_time = time.time()
    te3 = (end_time - start_time) * 1000
    print(f"T-E3: Tiempo para cifrar el texto: {te3} segundos")
    return encrypted_message, te3

def decrypt_message(encrypted_message, private_key):
    start_time = time.time()
    public_key_length = len(private_key.get_verifying_key().to_string().hex())
    decrypted_message = encrypted_message[public_key_length:]
    end_time = time.time()
    te4 = (end_time - start_time) * 1000
    print(f"T-E4: Tiempo para descifrar el texto: {te4} segundos")
    return decrypted_message, te4

# Leer archivo
file_path = '100p.txt'
message, te1 = read_file(file_path)

# Generar claves
private_key, public_key, te2 = generate_keys()
print(f"Private Key: {private_key.to_string().hex()}")
print(f"Public Key: {public_key.to_string().hex()}")

# Cifrar mensaje
encrypted_message, te3 = encrypt_message(message, public_key)
print(f"Encrypted Message: {encrypted_message}")

# Descifrar mensaje
decrypted_message, te4 = decrypt_message(encrypted_message, private_key)
print(f"Decrypted Message: {decrypted_message}")

# Número de palabras, caracteres de entrada y caracteres de salida
num_palabras = len(message.split())
num_caracteres_entrada = len(message)
num_caracteres_salida = len(encrypted_message)

# Tiempo total de ejecución
t_total = te1 + te2 + te3 + te4

# Imprimir resultados
print(f"Número de palabras: {num_palabras}")
print(f"Número de caracteres de entrada: {num_caracteres_entrada}")
print(f"Número de caracteres de salida: {num_caracteres_salida}")
print(f"T-E1: Tiempo de lectura de archivo: {te1} milisegundos")
print(f"T-E2: Tiempo de generación de claves: {te2} milisegundos")
print(f"T-E3: Tiempo para cifrar el texto: {te3} milisegundos")
print(f"T-E4: Tiempo para descifrar el texto: {te4} milisegundos")
print(f"T-Total: Tiempo total de ejecución: {t_total} milisegundos")

# Guardar resultados en un archivo
#with open('resultados.txt', 'w') as file:
 #   file.write(f"Número de palabras: {num_palabras}\n")
 #   file.write(f"Número de caracteres de entrada: {num_caracteres_entrada}\n")
 #   file.write(f"Número de caracteres de salida: {num_caracteres_salida}\n")
 #   file.write(f"T-E1: Tiempo de lectura de archivo: {te1} segundos\n")
 #   file.write(f"T-E2: Tiempo de generación de claves: {te2} segundos\n")
 #   file.write(f"T-E3: Tiempo para cifrar el texto: {te3} segundos\n")
 #   file.write(f"T-E4: Tiempo para descifrar el texto: {te4} segundos\n")
 #   file.write(f"T-Total: Tiempo total de ejecución: {t_total} segundos\n")