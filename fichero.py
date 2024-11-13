import requests

def descargar_datos(tipo):
    url = f'https://swapi.dev/api/{tipo}/'
    response = requests.get(url)
    if response.status_code == 200:
        datos = response.json()
        return datos['results']
    else:
        print(f'Error al descargar los datos: {response.status_code}')
        return []

def buscar_item(items, nombre, key):
    return [item for item in items if nombre.lower() in item[key].lower()]

def mostrar_menu():
    print("=======================================================================")
    print("1. Buscar personajes por nombre")
    print("2. Buscar planetas por nombre")
    print("3. Buscar vehículos por nombre")
    print("4. Salir")

def main():
    personajes = descargar_datos('people')
    planetas = descargar_datos('planets')
    vehiculos = descargar_datos('vehicles')

    if not personajes:
        print("Error al descargar los personajes.")
    else:
        print(f"Se descargaron {len(personajes)} personajes.")

    if not planetas:
        print("Error al descargar los planetas.")
    else:
        print(f"Se descargaron {len(planetas)} planetas.")

    if not vehiculos:
        print("Error al descargar los vehículos.")
    else:
        print(f"Se descargaron {len(vehiculos)} vehículos.")

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            nombre = input("Introduce el nombre del personaje: ")
            resultados = buscar_item(personajes, nombre, 'name')
            if resultados:
                for personaje in resultados:
                    print(f"Nombre: {personaje['name']}, Altura: {personaje['height']}, Peso: {personaje['mass']}, Color de ojos: {personaje['eye_color']}, Género: {personaje['gender']}")
            else:
                print("No se encontraron personajes con ese nombre.")
        
        elif opcion == '2':
            nombre = input("Introduce el nombre del planeta: ")
            resultados = buscar_item(planetas, nombre, 'name')
            if resultados:
                for planeta in resultados:
                    print(f"Nombre: {planeta['name']}, Clima: {planeta['climate']}, Terreno: {planeta['terrain']}")
            else:
                print("No se encontraron planetas con ese nombre.")
        
        elif opcion == '3':
            nombre = input("Introduce el nombre del vehículo: ")
            resultados = buscar_item(vehiculos, nombre, 'name')
            if resultados:
                for vehiculo in resultados:
                    print(f"Nombre: {vehiculo['name']}, Modelo: {vehiculo['model']}, Fabricante: {vehiculo['manufacturer']}, Costo: {vehiculo['cost_in_credits']}")
            else:
                print("No se encontraron vehículos con ese nombre.")
        
        elif opcion == '4':
            print("Saliendo...")
            break
        
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()
