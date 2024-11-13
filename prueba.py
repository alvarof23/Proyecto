import tkinter as tk

def saludo():
    print("¡Hola, Mundo!")

ventana = tk.Tk()
ventana.title("Mi Ventana")

boton = tk.Button(ventana, text="Saludar", command=saludo)
boton.pack()

ventana.mainloop()
