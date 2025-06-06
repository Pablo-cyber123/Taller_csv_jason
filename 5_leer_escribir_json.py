import json
import os

ARCHIVO = "productos.json"

def limpiar_consola():
    os.system("cls" if os.name == "nt" else "clear")

def cargar_productos():
    if not os.path.exists(ARCHIVO):
        return []
    try:
        with open(ARCHIVO, "r") as archivo:
            return json.load(archivo)
    except json.JSONDecodeError:
        print("El archivo de productos está dañado o vacío.")
        return []
    except Exception as e:
        print("Error al leer los productos:", e)
        return []

def guardar_productos(lista):
    try:
        with open(ARCHIVO, "w") as archivo:
            json.dump(lista, archivo, indent=2)
    except Exception as e:
        print("No se pudo guardar la información:", e)

def mostrar_productos():
    limpiar_consola()
    productos = cargar_productos()
    if not productos:
        print("No hay productos registrados.")
    else:
        print("\nListado de productos:")
        for prod in productos:
            print(f"ID: {prod['id']} | Nombre: {prod['nombre']} | Precio: ${prod['precio']:.2f} COP")
    input("\nPresione Enter para continuar...")

def agregar_producto():
    limpiar_consola()
    productos = cargar_productos()
    try:
        nuevo_id = int(input("Ingrese el ID del nuevo producto: "))
        nombre = input("Nombre del producto: ").strip()
        precio = float(input("Precio del producto en COP: "))
    except ValueError:
        print("Datos inválidos. Intente de nuevo.")
        input("Presione Enter para continuar...")
        return
    for prod in productos:
        if prod["id"] == nuevo_id:
            print("Ya existe un producto con ese ID.")
            input("Presione Enter para continuar...")
            return
    productos.append({"id": nuevo_id, "nombre": nombre, "precio": precio})
    guardar_productos(productos)
    print("Producto agregado correctamente.")
    input("Presione Enter para continuar...")

def main():
    while True:
        limpiar_consola()
        print("""
=== GESTIÓN DE PRODUCTOS ===

1. Ver productos almacenados
2. Agregar un nuevo producto
3. Salir
""")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            mostrar_productos()
        elif opcion == "2":
            agregar_producto()
        elif opcion == "3":
            print("Tenga un buen dia.")
            break
        else:
            print("Opción no válida.")
            input("Presione Enter para continuar...")

main()