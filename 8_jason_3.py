

import json
import os

ARCHIVO = "contacts.json"

def limpiar_consola():
    os.system("clear")

def cargar_contactos():
    if not os.path.exists(ARCHIVO):
        return []
    with open(ARCHIVO, "r") as archivo:
        try:
            return json.load(archivo)
        except json.JSONDecodeError:
            return []

def guardar_contactos(contactos):
    with open(ARCHIVO, "w") as archivo:
        json.dump(contactos, archivo, indent=4)

def validar_id(contactos, id_usuario):
    return any(str(contacto["ID"]) == str(id_usuario) for contacto in contactos)

def pedir_id():
    while True:
        id_usuario = input("Ingrese el ID (único, solo números) del usuario: ").strip()
        if id_usuario.isdigit():
            return id_usuario
        else:
            print("Error: El ID debe ser un número entero. Por favor, intente de nuevo.")

def pedir_texto(mensaje, solo_letras=True):
    while True:
        valor = input(mensaje).strip()
        if solo_letras:
            if valor.replace(" ", "").isalpha():
                return valor
            else:
                print("Error: Solo se permiten letras. Por favor, intente de nuevo.")
        else:
            if valor:
                return valor
            else:
                print("Error: Este campo no puede estar vacío.")

def pedir_telefono():
    while True:
        telefono = input("Ingrese el teléfono del usuario (solo números): ").strip()
        if telefono.isdigit():
            return telefono
        else:
            print("Error: El teléfono debe contener solo números. Intente de nuevo.")

def imprimir_contacto(contacto):
    print("{")
    print(f'    "ID": {contacto["ID"]},')
    print(f'    "Nombre": "{contacto["NOMBRE"]}",')
    print(f'    "Telefono": "{contacto["TELEFONO"]}",')
    print(f'    "Email": "{contacto["EMAIL"]}"')
    print("}")

def crear_contacto():
    limpiar_consola()
    contactos = cargar_contactos()
    try:
        id_usuario = pedir_id()
        if validar_id(contactos, id_usuario):
            print("Error: El ID ya existe.")
            return
        nombre = pedir_texto("Ingrese el nombre del usuario: ")
        ciudad = pedir_texto("Ingrese la ciudad del usuario: ")
        email = input("Ingrese el email del usuario: ").strip()
        telefono = pedir_telefono()
        if not (id_usuario and nombre and ciudad and email and telefono):
            print("Error: Todos los campos son obligatorios.")
            return
        contactos.append({
            "ID": id_usuario,
            "NOMBRE": nombre,
            "CIUDAD": ciudad,
            "EMAIL": email,
            "TELEFONO": telefono
        })
        guardar_contactos(contactos)
        print("Contacto agregado correctamente.")
    except Exception as e:
        print(f"Error al agregar contacto: {e}")

def leer_contactos():
    limpiar_consola()
    contactos = cargar_contactos()
    if not contactos:
        print("No hay contactos registrados.")
        return
    print("Lista de contactos:")
    for c in contactos:
        imprimir_contacto(c)

def filtrar_por_ciudad():
    limpiar_consola()
    contactos = cargar_contactos()
    if not contactos:
        print("No hay contactos registrados.")
        return
    ciudad = pedir_texto("Ingrese la ciudad para filtrar: ")
    filtrados = [c for c in contactos if c["CIUDAD"].strip().lower() == ciudad.strip().lower()]
    if filtrados:
        print(f"Contactos en {ciudad.title()}:")
        for c in filtrados:
            imprimir_contacto(c)
    else:
        print("No se encontraron contactos en esa ciudad.")

def actualizar_contacto():
    limpiar_consola()
    contactos = cargar_contactos()
    if not contactos:
        print("No hay contactos registrados.")
        return
    id_usuario = pedir_id()
    for c in contactos:
        if str(c["ID"]) == str(id_usuario):
            print("Contacto encontrado:")
            imprimir_contacto(c)
            print("""
¿Qué dato desea actualizar?
1. Nombre
2. Ciudad
3. Email
4. Teléfono
5. Cancelar
""")
            opcion = input("Seleccione una opción: ").strip()
            if opcion == "1":
                nuevo = pedir_texto(f"Nuevo nombre [{c['NOMBRE']}]: ")
                if nuevo:
                    c["NOMBRE"] = nuevo
            elif opcion == "2":
                nuevo = pedir_texto(f"Nueva ciudad [{c['CIUDAD']}]: ")
                if nuevo:
                    c["CIUDAD"] = nuevo
            elif opcion == "3":
                nuevo = input(f"Nuevo email [{c['EMAIL']}]: ").strip()
                if nuevo:
                    c["EMAIL"] = nuevo
            elif opcion == "4":
                nuevo = pedir_telefono()
                if nuevo:
                    c["TELEFONO"] = nuevo
            elif opcion == "5":
                print("Actualización cancelada.")
                return
            else:
                print("Opción inválida.")
                return
            guardar_contactos(contactos)
            print("Contacto actualizado correctamente.")
            return
    print("No se encontró un contacto con ese ID.")

def eliminar_contacto():
    limpiar_consola()
    contactos = cargar_contactos()
    if not contactos:
        print("No hay contactos registrados.")
        return
    id_usuario = pedir_id()
    nuevos_contactos = [c for c in contactos if str(c["ID"]) != str(id_usuario)]
    if len(nuevos_contactos) == len(contactos):
        print("No se encontró un contacto con ese ID.")
    else:
        guardar_contactos(nuevos_contactos)
        print("Contacto eliminado correctamente.")

def presione_enter():
    input("\nPresione Enter para continuar...")

def menu():
    while True:
        limpiar_consola()
        print("""
█▄─▀█▀─▄█▄─▄▄─█▄─▀█▄─▄█▄─██─▄█
██─█▄█─███─▄█▀██─█▄▀─███─██─██
▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▄▀▀▄▄▀▀▄▄▄▄▀▀
Menú de opciones:
1. Crear contacto
2. Leer todos los contactos
3. Filtrar contactos por ciudad
4. Actualizar contacto
5. Eliminar contacto
6. Salir
""")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            crear_contacto()
            presione_enter()
        elif opcion == "2":
            leer_contactos()
            presione_enter()
        elif opcion == "3":
            filtrar_por_ciudad()
            presione_enter()
        elif opcion == "4":
            actualizar_contacto()
            presione_enter()
        elif opcion == "5":
            eliminar_contacto()
            presione_enter()
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")
            presione_enter()

menu()