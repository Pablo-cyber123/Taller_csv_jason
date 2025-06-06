import csv
import json
import os

def limpiar_consola():
    os.system("cls" if os.name == "nt" else "clear")

def convertir_csv_a_json():
    limpiar_consola()
    print("=== Conversión de usuarios.csv a usuarios.json ===\n")
    
    # Antes de intentar leer el archivo, revisamos si realmente existe en la carpeta
    if not os.path.exists("usuarios.csv"):
        print("Atención: No se encontró el archivo usuarios.csv en la carpeta actual.")
        print("Por favor, asegúrese de que el archivo exista antes de continuar.")
        input("Presione Enter para volver al menú...")
        return

    try:
        # Abrimos el archivo CSV para leer los datos de los usuarios
        with open("usuarios.csv", "r", newline="") as archivo_csv:
            lector = csv.DictReader(archivo_csv)
            usuarios = list(lector)
            if not usuarios:
                print("El archivo usuarios.csv está vacío o no contiene datos válidos.")
                input("Presione Enter para volver al menú...")
                return
            print("Estos son los usuarios leídos desde el archivo CSV:")
            for usuario in usuarios:
                print(f"ID: {usuario['id']} | Nombre: {usuario['nombre']} | Ciudad: {usuario['ciudad']}")
    except Exception as e:
        print("Ocurrió un error al intentar leer el archivo CSV:", e)
        input("Presione Enter para volver al menú...")
        return

    try:
        # Ahora guardamos la lista de usuarios en un archivo JSON
        with open("usuarios.json", "w") as archivo_json:
            json.dump(usuarios, archivo_json, indent=2)
        print("\n¡Listo! Los datos se han guardado en usuarios.json en formato JSON.")
    except Exception as e:
        print("Ocurrió un error al guardar el archivo JSON:", e)
    input("Presione Enter para finalizar...")

def main():
    while True:
        limpiar_consola()
        print("""
========================================
 CONVERSOR DE USUARIOS CSV A JSON
========================================

1. Convertir usuarios.csv a usuarios.json
2. Salir
""")
        opcion = input("Seleccione una opción y presione Enter: ").strip()
        if opcion == "1":
            convertir_csv_a_json()
        elif opcion == "2":
            print("Gracias por usar el conversor. ¡Hasta la próxima!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
            input("Presione Enter para continuar...")


main()