import json
import os

ARCHIVO = "contacts.json"

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def cargar_lista():
    if not os.path.exists(ARCHIVO):
        return []
    with open(ARCHIVO, "r") as f:
        try:
            return json.load(f)
        except Exception:
            return []

def guardar_lista(contactos):
    with open(ARCHIVO, "w") as f:
        json.dump(contactos, f, indent=4)

def id_existe(contactos, id_buscar):
    return any(str(c["ID"]) == str(id_buscar) for c in contactos)

def pedir_id():
    while True:
        dato = input("ID (solo números): ").strip()
        if dato.isdigit():
            return dato
        print("El ID debe ser numérico.")

def pedir_texto(mensaje, solo_letras=True):
    while True:
        texto = input(mensaje).strip()
        if solo_letras:
            if texto.replace(" ", "").isalpha():
                return texto
            print("Solo se permiten letras.")
        else:
            if texto:
                return texto
            print("No puede estar vacío.")

def pedir_telefono():
    while True:
        tel = input("Teléfono (solo números): ").strip()
        if tel.isdigit():
            return tel
        print("El teléfono debe ser numérico.")

def mostrar_contacto(c):
    print(f"ID: {c['ID']}")
    print(f"Nombre: {c['NOMBRE']}")
    print(f"Ciudad: {c['CIUDAD']}")
    print(f"Email: {c['EMAIL']}")
    print(f"Telefono: {c['TELEFONO']}")
    print("-" * 30)

def agregar_contacto():
    limpiar_pantalla()
    contactos = cargar_lista()
    id_nuevo = pedir_id()
    if id_existe(contactos, id_nuevo):
        print("Ese ID ya está registrado.")
        return
    nombre = pedir_texto("Nombre: ")
    ciudad = pedir_texto("Ciudad: ")
    email = input("Email: ").strip()
    telefono = pedir_telefono()
    if not (id_nuevo and nombre and ciudad and email and telefono):
        print("Todos los campos son obligatorios.")
        return
    contactos.append({
        "ID": id_nuevo,
        "NOMBRE": nombre,
        "CIUDAD": ciudad,
        "EMAIL": email,
        "TELEFONO": telefono
    })
    guardar_lista(contactos)
    print("Contacto guardado.")

def ver_contactos():
    limpiar_pantalla()
    contactos = cargar_lista()
    if not contactos:
        print("No hay contactos.")
        return
    print("Contactos registrados:")
    for c in contactos:
        mostrar_contacto(c)

def buscar_por_ciudad():
    limpiar_pantalla()
    contactos = cargar_lista()
    if not contactos:
        print("No hay contactos.")
        return
    ciudad = pedir_texto("Ciudad a buscar: ")
    resultado = [c for c in contactos if c["CIUDAD"].strip().lower() == ciudad.strip().lower()]
    if resultado:
        print(f"Contactos en {ciudad.title()}:")
        for c in resultado:
            mostrar_contacto(c)
    else:
        print("No se hallaron contactos en esa ciudad.")

def editar_contacto():
    limpiar_pantalla()
    contactos = cargar_lista()
    if not contactos:
        print("No hay contactos.")
        return
    id_mod = pedir_id()
    for c in contactos:
        if str(c["ID"]) == str(id_mod):
            print("Contacto actual:")
            mostrar_contacto(c)
            print("""
¿Qué desea modificar?
1. Nombre
2. Ciudad
3. Email
4. Teléfono
5. Cancelar
""")
            op = input("Opción: ").strip()
            if op == "1":
                nuevo = pedir_texto(f"Nuevo nombre [{c['NOMBRE']}]: ")
                if nuevo:
                    c["NOMBRE"] = nuevo
            elif op == "2":
                nuevo = pedir_texto(f"Nueva ciudad [{c['CIUDAD']}]: ")
                if nuevo:
                    c["CIUDAD"] = nuevo
            elif op == "3":
                nuevo = input(f"Nuevo email [{c['EMAIL']}]: ").strip()
                if nuevo:
                    c["EMAIL"] = nuevo
            elif op == "4":
                nuevo = pedir_telefono()
                if nuevo:
                    c["TELEFONO"] = nuevo
            elif op == "5":
                print("Edición cancelada.")
                return
            else:
                print("Opción no válida.")
                return
            guardar_lista(contactos)
            print("Contacto actualizado.")
            return
    print("No existe un contacto con ese ID.")

def borrar_contacto():
    limpiar_pantalla()
    contactos = cargar_lista()
    if not contactos:
        print("No hay contactos.")
        return
    id_borrar = pedir_id()
    nuevos = [c for c in contactos if str(c["ID"]) != str(id_borrar)]
    if len(nuevos) == len(contactos):
        print("No se encontró ese ID.")
    else:
        guardar_lista(nuevos)
        print("Contacto eliminado.")

def esperar_enter():
    input("\nPulse Enter para continuar...")

def menu_principal():
    while True:
        limpiar_pantalla()
        print("""
=============================================================================================
████─████─███─█──█─████──████────████──███────████─████─█──█─███─████─████─███─████─███
█──█─█────█───██─█─█──██─█──█────█──██─█──────█──█─█──█─██─█──█──█──█─█──█──█──█──█─█──
████─█─██─███─█─██─█──██─████────█──██─███────█────█──█─█─██──█──████─█─────█──█──█─███
█──█─█──█─█───█──█─█──██─█──█────█──██─█──────█──█─█──█─█──█──█──█──█─█──█──█──█──█───█
█──█─████─███─█──█─████──█──█────████──███────████─████─█──█──█──█──█─████──█──████─███
=============================================================================================
1. Añadir contacto
2. Ver todos los contactos
3. Buscar por ciudad
4. Editar contacto
5. Eliminar contacto
6. Salir
""")
        op = input("Elija una opción: ").strip()
        if op == "1":
            agregar_contacto()
            esperar_enter()
        elif op == "2":
            ver_contactos()
            esperar_enter()
        elif op == "3":
            buscar_por_ciudad()
            esperar_enter()
        elif op == "4":
            editar_contacto()
            esperar_enter()
        elif op == "5":
            borrar_contacto()
            esperar_enter()
        elif op == "6":
            print("Programa finalizado.")
            break
        else:
            print("Opción incorrecta.")
            esperar_enter()


menu_principal()