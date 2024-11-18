import tkinter as tk
from tkinter import simpledialog

# Funcion para encriptar el texto desplazando caracteres
def encrypt(text, shift):
    original_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    shifted_alphabet = original_alphabet[shift:] + original_alphabet[:shift]
    table = str.maketrans(original_alphabet + original_alphabet.lower(), shifted_alphabet + shifted_alphabet.lower())
    encrypted_text = text.translate(table)
    return original_alphabet, shifted_alphabet, encrypted_text

def main():
    root = tk.Tk()
    root.withdraw()  
    # Solicitar el mensaje y el numero de caracteres a recorrer
    text = simpledialog.askstring("Mensaje", "Ingrese el mensaje:")
    shift = simpledialog.askinteger("Numero", "Ingrese los caracteres a recorrer:")

    if text is not None and shift is not None:
        original_alphabet, shifted_alphabet, encrypted_text = encrypt(text, shift)

        result_window = tk.Toplevel(root)
        result_window.title("Resultado")
        
        # Mostrar los resultados incluyendo el alfabeto original y el desplazado
        tk.Label(result_window, text=f"Alfabeto Original: {original_alphabet}").pack()
        tk.Label(result_window, text=f"Alfabeto Desplazado: {shifted_alphabet}").pack()
        tk.Label(result_window, text=f"Texto Original: {text}").pack()
        tk.Label(result_window, text=f"Texto Desplazado: {encrypted_text}").pack()
        tk.Button(result_window, text="Close", command=result_window.destroy).pack()

        result_window.mainloop()

if __name__ == "__main__":
    main()