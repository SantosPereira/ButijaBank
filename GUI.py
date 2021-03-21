import tkinter as tk
import sys

def janela(message):
    window = tk.Tk()
    window.title("Butija Bank S/A")
    window.geometry("800x500")
    texto = tk.Label(text=message, width=300, height=300)
    texto.pack()

    window.mainloop()

janela('FUNCIONOU')
# janela(sys.argv[1])
# janela(sys.stdin)
