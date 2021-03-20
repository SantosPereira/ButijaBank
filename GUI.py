import tkinter as tk

def janela(message):
    window = tk.Tk()
    window.title("Butija Bank S/A")
    window.geometry("800x500")
    texto = tk.Label(text=message, width=300, height=300)
    texto.pack()

    window.mainloop()

janela('texto')