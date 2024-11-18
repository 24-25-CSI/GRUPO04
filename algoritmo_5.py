import tkinter as tk
from tkinter import messagebox

def generar_clave(palabra, clave):
    clave = clave * (len(palabra) // len(clave) + 1)
    return clave[:len(palabra)]

def encriptacion_vigenere(palabra, clave):
    clave = generar_clave(palabra, clave)
    encriptar_texto = []
    for p, c in zip(palabra, clave):
        encriptar_caracter = chr(((ord(p) + ord(c)) % 26) + ord('A'))
        encriptar_texto.append(encriptar_caracter)
    return ''.join(encriptar_texto)

def decencriptar_vigenere(cifrado, clave):
    clave = generar_clave(cifrado, clave)
    decencriptar_texto = []
    for ci, cl in zip(cifrado, clave):
        decencriptar_caracter = chr(((ord(ci) - ord(cl) + 26) % 26) + ord('A'))
        decencriptar_texto.append(decencriptar_caracter)
    return ''.join(decencriptar_texto)

def cifrar():
    palabra = palabra_entry.get().upper()
    clave = clave_entry.get().upper()
    if not palabra.isalpha() or not clave.isalpha():
        messagebox.showerror("Error", "Solo se permiten letras en palabra y clave.")
        return
    encriptado = encriptacion_vigenere(palabra, clave)
    resultado_label.config(text=f"Texto cifrado: {encriptado}")

def descifrar():
    cifrado = palabra_entry.get().upper()
    clave = clave_entry.get().upper()
    if not cifrado.isalpha() or not clave.isalpha():
        messagebox.showerror("Error", "Solo se permiten letras en cifrado y clave.")
        return
    descifrado = decencriptar_vigenere(cifrado, clave)
    resultado_label.config(text=f"Texto descifrado: {descifrado}")

# interfaz gráfica
root = tk.Tk()
root.title("Cifrado Vigenère")

tk.Label(root, text="Palabra o Texto Cifrado:").grid(row=0, column=0)
palabra_entry = tk.Entry(root)
palabra_entry.grid(row=0, column=1)

tk.Label(root, text="Clave:").grid(row=1, column=0)
clave_entry = tk.Entry(root)
clave_entry.grid(row=1, column=1)

cifrar_button = tk.Button(root, text="Cifrar", command=cifrar)
cifrar_button.grid(row=2, column=0)

descifrar_button = tk.Button(root, text="Descifrar", command=descifrar)
descifrar_button.grid(row=2, column=1)

resultado_label = tk.Label(root, text="Resultado:")
resultado_label.grid(row=3, column=0, columnspan=2)

root.mainloop()
