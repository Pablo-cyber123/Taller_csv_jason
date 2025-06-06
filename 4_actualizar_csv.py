#'''4. **Actualizar un CSV (lectura-escritura)**
#
#   - Lee `usuarios.csv` y modifica la ciudad de un usuario dado (ej. cambiar al usuario con `id=3` a ciudad “Cali”).
#   - Sobrescribe el mismo archivo con los cambios.
#   - Asegúrate de usar un bloque `try-except` para capturar errores de lectura/escritura.'''

import csv
import os

def limpiar_consola():
    os.system("cls" if os.name == "nt" else "clear")

def pedir_datos():
    limpiar_consola()
    try:
        cantidad = int(input('¿Cuántos usuarios desea registrar? '))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return
    usuarios = []
    for i in range(cantidad):
        id_usuario = input(f"Ingrese el ID del usuario {i + 1}: ").strip()
        nombre = input(f"Ingrese el nombre del usuario {i + 1}: ").strip()
        ciudad = input(f"Ingrese la ciudad del usuario {i + 1}: ").strip()
        usuarios.append({"id": id_usuario, "nombre": nombre, "ciudad": ciudad})

    try:
        with open("usuarios.csv", "a", newline="") as archivo:
            campos = ["id", "nombre", "ciudad"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            archivo.seek(0, 2)
            if archivo.tell() == 0:
                escritor.writeheader()
            escritor.writerows(usuarios)
        print("Usuarios registrados correctamente.")
    except Exception as e:
        print("Ocurrió un error al guardar los usuarios:", e)

def leer_usuarios_y_filtrar():
    limpiar_consola()
    try:
        with open("usuarios.csv", newline="") as archivo:
            lector = csv.DictReader(archivo)
            ciudad = input('Ingrese la ciudad por la que desea filtrar: ').strip().lower()
            encontrados = [usuario for usuario in lector if usuario["ciudad"].strip().lower() == ciudad]
            if encontrados:
                print(f"\nUsuarios registrados en {ciudad.title()}:")
                for usuario in encontrados:
                    print(f"ID: {usuario['id']} | Nombre: {usuario['nombre']} | Ciudad: {usuario['ciudad']}")
            else:
                print("No se encontraron usuarios en la ciudad indicada.")
    except FileNotFoundError:
        print("El archivo usuarios.csv no existe. Registre usuarios primero.")
    except Exception as e:
        print("Ocurrió un error al leer los usuarios:", e)

def mostrar_todos_los_usuarios():
    limpiar_consola()
    try:
        with open("usuarios.csv", newline="") as archivo:
            lector = csv.DictReader(archivo)
            usuarios = list(lector)
            if usuarios:
                print("\nLista de todos los usuarios registrados:")
                for usuario in usuarios:
                    print(f"ID: {usuario['id']} | Nombre: {usuario['nombre']} | Ciudad: {usuario['ciudad']}")
            else:
                print("No hay usuarios registrados para mostrar.")
    except FileNotFoundError:
        print("El archivo usuarios.csv no existe. Registre usuarios primero.")
    except Exception as e:
        print("Ocurrió un error al leer los usuarios:", e)

def actualizar_usuario():
    limpiar_consola()
    try:
        with open("usuarios.csv", newline="") as archivo:
            lector = list(csv.DictReader(archivo))
    except FileNotFoundError:
        print("No se encontró el archivo de usuarios. Por favor, registre usuarios primero.")
        return

    if not lector:
        print("No hay usuarios registrados para actualizar.")
        return

    id_buscar = input("Ingrese el ID del usuario que desea actualizar: ").strip()
    usuario_encontrado = None
    for usuario in lector:
        if usuario["id"] == id_buscar:
            usuario_encontrado = usuario
            break

    if not usuario_encontrado:
        print("No se encontró un usuario con ese ID.")
        return

    print(f"\nUsuario encontrado:\nID: {usuario_encontrado['id']}, Nombre: {usuario_encontrado['nombre']}, Ciudad: {usuario_encontrado['ciudad']}")
    print("""
¿Qué dato desea modificar?
1. Nombre
2. Ciudad
3. Cancelar
""")
    opcion = input("Seleccione una opción: ").strip()
    if opcion == "1":
        nuevo_nombre = input(f"Ingrese el nuevo nombre [{usuario_encontrado['nombre']}]: ").strip()
        if nuevo_nombre:
            usuario_encontrado["nombre"] = nuevo_nombre
    elif opcion == "2":
        nueva_ciudad = input(f"Ingrese la nueva ciudad [{usuario_encontrado['ciudad']}]: ").strip()
        if nueva_ciudad:
            usuario_encontrado["ciudad"] = nueva_ciudad
    elif opcion == "3":
        print("Actualización cancelada.")
        return
    else:
        print("Opción inválida.")
        return

    try:
        with open("usuarios.csv", "w", newline="") as archivo:
            campos = ["id", "nombre", "ciudad"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(lector)
        print("La información del usuario ha sido actualizada correctamente.")
    except Exception as e:
        print("Ocurrió un error al guardar los cambios:", e)

def presione_ent():
    input('\nPresione Enter para continuar...')

def main():
    while True:
        limpiar_consola()
        menu = '''
█▄─▀█▀─▄█▄─▄▄─█▄─▀█▄─▄█▄─██─▄█
██─█▄█─███─▄█▀██─█▄▀─███─██─██
▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▄▀▀▄▄▀▀▄▄▄▄▀▀
Introduce la acción que desea realizar:
1. Escribir base de datos
2. Filtrar usuarios por ciudad
3. Actualizar usuario
4. Mostrar todos los usuarios
5. Salir
'''
        print(menu)
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            pedir_datos()
            presione_ent()
        elif opcion == "2":
            leer_usuarios_y_filtrar()
            presione_ent()
        elif opcion == "3":
            actualizar_usuario()
            presione_ent()
        elif opcion == "4":
            mostrar_todos_los_usuarios()
            presione_ent()
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Por favor, intente nuevamente.")
            presione_ent()

main()