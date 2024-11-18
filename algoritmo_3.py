import tkinter as tk
from tkinter import simpledialog, messagebox

def columnar_transposition_cipher(message, n):
    # Eliminar espacios en el mensaje
    message = message.replace(" ", "")
    
    # Comprobar que el mensaje sea menor o igual a n*n
    if len(message) > n * n:
        raise ValueError("La longitud del mensaje debe ser menor o igual a n * n")
    
    # Rellenar con '*' hasta que el mensaje alcance la longitud n*n
    while len(message) < n * n:
        message += '*'
    
    # Crear la matriz de n x n llenando por columnas
    matrix = [['' for _ in range(n)] for _ in range(n)]
    index = 0
    for col in range(n):
        for row in range(n):
            matrix[row][col] = message[index]
            index += 1
    
    # Leer por filas para obtener el mensaje cifrado
    ciphered_message = ""
    for row in range(n):
        for col in range(n):
            ciphered_message += matrix[row][col]
    
    return message, ciphered_message, matrix

def display_matrix(matrix):
    # Convertir la matriz a una cadena de texto para mostrar
    matrix_str = "\n".join([" ".join(row) for row in matrix])
    messagebox.showinfo("Matriz", f"Matriz {len(matrix)}x{len(matrix)}:\n{matrix_str}")

def get_input():
    # Crear ventana para pedir el mensaje y el tamaño de la matriz
    root = tk.Tk()
    root.withdraw()  

    message = simpledialog.askstring("Mensaje", "Ingrese el mensaje:")
    n = simpledialog.askinteger("N", "Ingrese el tamaño de la matriz:")

    return message, n

def main():
    try:
        message, n = get_input()

        # Realizar la transposición de columnas
        original_message, ciphered_message, matrix = columnar_transposition_cipher(message, n)

        # Mostrar la matriz
        display_matrix(matrix)

        # Mostrar los resultados
        result_message = f"Mensaje original: {original_message}\nMensaje cifrado: {ciphered_message}"
        messagebox.showinfo("Resultado", result_message)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    main()
