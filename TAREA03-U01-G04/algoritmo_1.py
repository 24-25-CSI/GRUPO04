import tkinter as tk
from tkinter import messagebox
from itertools import permutations

def anagramas():
    palabra = entry.get()
    # Generar todas las permutaciones 
    permutaciones = sorted(set([''.join(p) for p in permutations(palabra)]))
    total_permutaciones = len(permutaciones)
    

    resultado = f"Número total de permutaciones: {total_permutaciones}\n"
    resultado += "Las primeras 10 permutaciones son:\n" + '\n'.join(permutaciones[:10])
    messagebox.showinfo("Resultado", resultado)


root = tk.Tk()
root.title("Generador de Anagramas")

label = tk.Label(root, text="Ingrese una palabra:")
label.pack(pady=10)

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

button = tk.Button(root, text="Generar Anagramas", command=anagramas)
button.pack(pady=20)

root.mainloop()
