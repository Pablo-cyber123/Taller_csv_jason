def limpiar_consola():
    import os
    os.system("cls" if os.name == "nt" else "clear")

def pedir_nombre():
    while True:
        nombre = input("¿Cómo te llamas? ").strip()
        if nombre:
            return nombre
        print("Ups, escribe tu nombre para continuar.")

def pedir_edad():
    while True:
        edad_str = input("¿Cuántos años tienes? ").strip()
        try:
            edad = int(edad_str)
            return edad
        except ValueError:
            print("Eso no es un número. Intenta escribir solo tu edad con números.")

def mostrar_resultado(nombre, edad):
    try:
        mensaje = "La edad de " + nombre + " es " + edad
    except TypeError:
        mensaje = "La edad de " + nombre + " es " + str(edad)
    print("\n" + mensaje)
    input("\nPresiona Enter para volver al menú...")

def menu_principal():
    while True:
        limpiar_consola()
        print("""
===============================
¡Bienvenido al juego de edades!
===============================

1. Escribir mi nombre y mi edad
2. Salir
""")
        opcion = input("Elige una opción (1 o 2): ").strip()
        if opcion == "1":
            limpiar_consola()
            print("¡Vamos a jugar!\n")
            nombre = pedir_nombre()
            edad = pedir_edad()
            mostrar_resultado(nombre, edad)
        elif opcion == "2":
            print("¡Adiós! Que tengas un día divertido.")
            break
        else:
            print("Esa opción no existe. Intenta otra vez.")
            input("Presiona Enter para seguir...")

menu_principal()