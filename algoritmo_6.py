# Ejercicio 6: Cifrado de un mensaje utilizando una tabla de cifrado
# Algoritmo que realice el cifrado de una cadena de caracteres utilizando una tabla de cifrado
#La cadena de caracteres se ingresa al iniciar el programa. 
# Si algún caracter del texto no existe en la matriz, coloque"**". 
# Imprima la matriz de cifrado, el mensaje original y el mensaje cifrado.
# Definición de la tabla de cifrado en un diccionario

import tkinter as tk
from tkinter import messagebox

# Tabla de cifrado
tabla_cifrado = {
    'a': 'QA', 'b': 'QS', 'c': 'QD', 'd': 'QF', 'e': 'QG',
    'f': 'WA', 'g': 'WS', 'h': 'WD', 'i': 'WF', 'j': 'WG',
    'k': 'EA', 'l': 'ES', 'm': 'ED', 'n': 'EF', 'o': 'EG',
    'p': 'RA', 'q': 'RS', 'r': 'RD', 's': 'RF', 't': 'RG',
    'u': 'TA', 'v': 'TS', 'w': 'TD', 'x': 'TF', 'y': 'TG',
    'z': 'UA'
}

def cifrar_mensaje(mensaje):
    mensaje_cifrado = []
    for caracter in mensaje:
        if caracter in tabla_cifrado:
            mensaje_cifrado.append(tabla_cifrado[caracter])
        else:
            mensaje_cifrado.append("**")  # Caracter no encontrado
    return " ".join(mensaje_cifrado)

def realizar_cifrado():
    mensaje_original = entrada_mensaje.get().lower()
    if not mensaje_original.isalpha():
        messagebox.showerror("Error", "El mensaje solo debe contener letras.")
        return
    mensaje_cifrado = cifrar_mensaje(mensaje_original)
    resultado_label.config(text=f"Mensaje cifrado: {mensaje_cifrado}")

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Cifrado Personalizado")

tk.Label(root, text="Ingresa el mensaje a cifrar:").grid(row=0, column=0)
entrada_mensaje = tk.Entry(root, width=30)
entrada_mensaje.grid(row=0, column=1)

cifrar_button = tk.Button(root, text="Cifrar", command=realizar_cifrado)
cifrar_button.grid(row=1, column=0, columnspan=2)

resultado_label = tk.Label(root, text="Mensaje cifrado:")
resultado_label.grid(row=2, column=0, columnspan=2)

root.mainloop()
