import tkinter as tk
from tkinter import messagebox
import numpy as np

def cifrado_filas():
    mensaje = entry_mensaje.get().replace(" ", "")
    try:
        filas = int(entry_filas.get())
    except ValueError:
        messagebox.showerror("Error", "El número de filas debe ser un número entero.")
        return
    
    # Controlar la longitud del mensaje
    if len(mensaje) > filas * filas:
        messagebox.showerror("Error", "El mensaje es demasiado largo para la matriz de cifrado.")
        return
    
    # Rellenar el mensaje con '*' si es necesario
    mensaje += '*' * (filas * filas - len(mensaje))
    
    # Crear y transponer la matriz de cifrado
    matriz = np.array(list(mensaje)).reshape(filas, filas)
    matriz_transpuesta = matriz.T
    mensaje_cifrado = ''.join(matriz_transpuesta.flatten())
    
    resultado = "Matriz de cifrado:\n" + '\n'.join(' '.join(fila) for fila in matriz)
    resultado += f"\n\nMensaje original: {mensaje}\nMensaje cifrado: {mensaje_cifrado}"
    

    messagebox.showinfo("Resultado", resultado)


root = tk.Tk()
root.title("Cifrado por Permutación de Filas")

tk.Label(root, text="Ingrese el mensaje:").pack(pady=5)
entry_mensaje = tk.Entry(root, width=30)
entry_mensaje.pack(pady=5)

tk.Label(root, text="Ingrese el número de filas:").pack(pady=5)
entry_filas = tk.Entry(root, width=10)
entry_filas.pack(pady=5)

tk.Button(root, text="Cifrar Mensaje", command=cifrado_filas).pack(pady=20)


root.mainloop()
