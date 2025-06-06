import csv

def pedir_datos():
    ent = int(input('Ingrese cuántos datos de personas va a ingresar: '))
    usuarios = [] 
    for i in range(ent):
        id_usuario = input(f"Ingrese el ID del usuario {i + 1}: ")
        nombre = input(f"Ingrese el nombre del usuario {i + 1}: ")
        ciudad = input(f"Ingrese la ciudad del usuario {i + 1}: ")
        usuarios.append({"id": id_usuario, "nombre": nombre, "ciudad": ciudad})

    # Escribir los datos en el archivo CSV
    with open("usuarios.csv", "a", newline="") as archivo:
        campos = ["id", "nombre", "ciudad"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        archivo.seek(0, 2) 
        if archivo.tell() == 0:  
            escritor.writeheader()
        escritor.writerows(usuarios)

def leer_usuarios_y_filtar():
    try:
        with open("usuarios.csv", newline="") as archivo:
            lector = csv.DictReader(archivo)
            city = input('Ingrese por cuál ciudad quiere filtrar la información: ').lower()
            usuarios_filtrados = [usuario for usuario in lector if usuario["ciudad"].lower() == city]
            
            if usuarios_filtrados:
                for usuario in usuarios_filtrados:
                    print(f"ID: {usuario['id']}, Nombre: {usuario['nombre']}, Ciudad: {usuario['ciudad']}")
            else:
                print("No se encontraron usuarios en la ciudad especificada.")
    except FileNotFoundError:
        print("El archivo usuarios.csv no se encuentra. Por favor, asegúrate de que el archivo existe.")

def presione_ent():
    input('Presione enter si desea continuar')

def main():
    while True:
        menu = '''
█▄─▀█▀─▄█▄─▄▄─█▄─▀█▄─▄█▄─██─▄█
██─█▄█─███─▄█▀██─█▄▀─███─██─██
▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▄▀▀▄▄▀▀▄▄▄▄▀▀
Introduce la acción que desea realizar:
1. Escribir base de datos
2. Filtrar usuarios por ciudad
3. Salir
'''
        print(menu)
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            pedir_datos()
            presione_ent()
        elif opcion == "2":
            leer_usuarios_y_filtar()
            presione_ent()
        elif opcion == "3":
            break
        else:
            print("Opción inválida. Por favor, intente nuevamente.")

main()
