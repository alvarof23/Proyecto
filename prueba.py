import requests
import tkinter as tk
from tkinter import messagebox, simpledialog

def descargar_datos(tipo):
    url = f'https://swapi.dev/api/{tipo}/'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['results']
    else:
        messagebox.showerror("Error", f"Error al descargar los datos: {response.status_code}")
        return []

def buscar_item(items, nombre, key):
    return [item for item in items if nombre.lower() in item[key].lower()]

def mostrar_resultados(resultados, tipo):
    if resultados:
        mensaje = ""
        for item in resultados:
            if tipo == 'personajes':
                mensaje += f"Nombre: {item['name']} \nAltura: {item['height']} \nPeso: {item['mass']} \nOjos: {item['eye_color']} \nGénero: {item['gender']}\n"
            elif tipo == 'planetas':
                mensaje += f"Nombre: {item['name']} \nClima: {item['climate']} \nTerreno: {item['terrain']}\n"
            elif tipo == 'vehículos':
                mensaje += f"Nombre: {item['name']} \nModelo: {item['model']} \nFabricante: {item['manufacturer']} \nCosto: {item['cost_in_credits']}\n"
        messagebox.showinfo("Resultados", mensaje)
    else:
        messagebox.showinfo("Sin resultados", f"No se encontraron {tipo} con ese nombre.")

def buscar(tipo):
    nombre = simpledialog.askstring("Buscar", f"Introduce el nombre del {tipo[:-1]}:")
    if nombre:
        if tipo == 'personajes':
            resultados = buscar_item(personajes, nombre, 'name')
            mostrar_resultados(resultados, 'personajes')
        elif tipo == 'planetas':
            resultados = buscar_item(planetas, nombre, 'name')
            mostrar_resultados(resultados, 'planetas')
        elif tipo == 'vehículos':
            resultados = buscar_item(vehiculos, nombre, 'name')
            mostrar_resultados(resultados, 'vehículos')

# Descargar datos al inicio
personajes = descargar_datos('people')
planetas = descargar_datos('planets')
vehiculos = descargar_datos('vehicles')

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Star Wars Data Browser")
ventana.geometry("300x200")

# Botones de búsqueda
btn_personajes = tk.Button(ventana, text="Buscar personajes", command=lambda: buscar('personajes'))
btn_personajes.pack(pady=10)

btn_planetas = tk.Button(ventana, text="Buscar planetas", command=lambda: buscar('planetas'))
btn_planetas.pack(pady=10)

btn_vehiculos = tk.Button(ventana, text="Buscar vehículos", command=lambda: buscar('vehículos'))
btn_vehiculos.pack(pady=10)

# Botón para salir
btn_salir = tk.Button(ventana, text="Salir", command=ventana.quit)
btn_salir.pack(pady=10)

# Ejecutar la aplicación
ventana.mainloop()
